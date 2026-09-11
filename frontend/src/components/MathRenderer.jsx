import React from 'react';
import katex from 'katex';

/**
 * Helper to render inline KaTeX math ($...$) safely
 */
function renderMathOnly(text, keyPrefix) {
  if (!text) return null;
  const parts = [];
  const mathRegex = /\$([^\$]+)\$/g;
  let lastIdx = 0;
  let m;

  while ((m = mathRegex.exec(text)) !== null) {
    if (m.index > lastIdx) {
      parts.push(text.substring(lastIdx, m.index));
    }
    const expr = m[1];
    try {
      const html = katex.renderToString(expr, {
        displayMode: false,
        throwOnError: false,
      });
      parts.push(
        <span
          key={`${keyPrefix}-m-${m.index}`}
          className="inline-block px-1 align-baseline"
          dangerouslySetInnerHTML={{ __html: html }}
        />
      );
    } catch {
      parts.push(<code key={`${keyPrefix}-m-${m.index}`}>{expr}</code>);
    }
    lastIdx = m.index + m[0].length;
  }

  if (lastIdx < text.length) {
    parts.push(text.substring(lastIdx));
  }

  return parts.length > 0 ? parts : text;
}

/**
 * Helper to render bold (**...**) and inline KaTeX math ($...$) seamlessly
 */
function renderFormattedInline(text, keyPrefix) {
  if (!text) return null;
  const parts = [];
  const boldRegex = /\*\*([^*]+)\*\*/g;
  let lastIdx = 0;
  let m;

  while ((m = boldRegex.exec(text)) !== null) {
    if (m.index > lastIdx) {
      parts.push(renderMathOnly(text.substring(lastIdx, m.index), `${keyPrefix}-txt-${m.index}`));
    }
    const boldInner = m[1];
    parts.push(
      <strong key={`${keyPrefix}-b-${m.index}`} className="font-bold text-slate-900">
        {renderMathOnly(boldInner, `${keyPrefix}-binner-${m.index}`)}
      </strong>
    );
    lastIdx = m.index + m[0].length;
  }

  if (lastIdx < text.length) {
    parts.push(renderMathOnly(text.substring(lastIdx), `${keyPrefix}-tail`));
  }

  return parts.length > 0 ? parts : renderMathOnly(text, keyPrefix);
}

/**
 * MathRenderer component: Parses ChatGPT-style markdown with full KaTeX support
 */
export default function MathRenderer({ content = '' }) {
  if (!content) return null;

  // Split content into blocks by $$...$$ block math
  const tokens = [];
  const blockMathRegex = /\$\$([\s\S]*?)\$\$/g;
  let lastIndex = 0;
  let match;

  while ((match = blockMathRegex.exec(content)) !== null) {
    if (match.index > lastIndex) {
      tokens.push({ type: 'text', value: content.substring(lastIndex, match.index) });
    }
    tokens.push({ type: 'blockMath', value: match[1].trim() });
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < content.length) {
    tokens.push({ type: 'text', value: content.substring(lastIndex) });
  }

  return (
    <div className="math-rendered text-slate-800 space-y-2">
      {tokens.map((token, tokenIdx) => {
        if (token.type === 'blockMath') {
          try {
            const html = katex.renderToString(token.value, {
              displayMode: true,
              throwOnError: false,
            });
            return (
              <div
                key={`bm-${tokenIdx}`}
                className="my-3 py-2 px-3 overflow-x-auto text-center rounded-xl bg-white/60 border border-slate-100 shadow-2xs"
                dangerouslySetInnerHTML={{ __html: html }}
              />
            );
          } catch {
            return (
              <div key={`bm-${tokenIdx}`} className="font-mono text-center my-3 text-slate-800">
                {token.value}
              </div>
            );
          }
        }

        // Token is text: split by lines
        const lines = token.value.split('\n');
        return (
          <React.Fragment key={`txt-blk-${tokenIdx}`}>
            {lines.map((line, lineIdx) => {
              const trimmed = line.trim();
              const fullKey = `t-${tokenIdx}-l-${lineIdx}`;

              // Empty lines
              if (!trimmed) {
                return <div key={fullKey} className="h-1" />;
              }

              // Horizontal divider
              if (trimmed === '---') {
                return <hr key={fullKey} className="my-5 border-t border-slate-200" />;
              }

              // Headings
              if (line.startsWith('### ')) {
                const headingText = line.replace('### ', '');
                const isFinal = headingText.includes('Final Answer') || headingText.includes('సమాధానం');
                return (
                  <h3
                    key={fullKey}
                    className={`text-lg sm:text-xl font-bold flex items-center gap-2 mt-4 mb-2 ${
                      isFinal ? 'text-emerald-700' : 'text-slate-900'
                    }`}
                  >
                    {renderFormattedInline(headingText, `${fullKey}-h3`)}
                  </h3>
                );
              }

              if (line.startsWith('## ')) {
                return (
                  <h2 key={fullKey} className="text-xl font-extrabold text-slate-900 mt-5 mb-3">
                    {renderFormattedInline(line.replace('## ', ''), `${fullKey}-h2`)}
                  </h2>
                );
              }

              // Numbered lists (1. 2. 3.)
              const numberedMatch = trimmed.match(/^(\d+)\.\s+(.*)$/);
              if (numberedMatch) {
                return (
                  <div key={fullKey} className="flex items-start gap-2.5 my-1.5 pl-2 text-slate-800 text-sm sm:text-base leading-relaxed">
                    <span className="font-bold text-amber-900 select-none min-w-[20px]">{numberedMatch[1]}.</span>
                    <div className="flex-1">
                      {renderFormattedInline(numberedMatch[2], `${fullKey}-num`)}
                    </div>
                  </div>
                );
              }

              // Bullet points
              const isBullet = trimmed.startsWith('•') || trimmed.startsWith('- ') || trimmed.startsWith('* ');
              if (isBullet) {
                const bulletContent = trimmed.replace(/^[•\-*]\s*/, '');
                return (
                  <div key={fullKey} className="flex items-start gap-2.5 my-1.5 pl-2 text-slate-800 text-sm sm:text-base leading-relaxed">
                    <span className="text-amber-600 font-bold select-none text-base leading-none mt-1">•</span>
                    <div className="flex-1">
                      {renderFormattedInline(bulletContent, `${fullKey}-bul`)}
                    </div>
                  </div>
                );
              }

              // Regular paragraph
              return (
                <p key={fullKey} className="my-1.5 text-slate-800 text-sm sm:text-base leading-relaxed">
                  {renderFormattedInline(line, `${fullKey}-p`)}
                </p>
              );
            })}
          </React.Fragment>
        );
      })}
    </div>
  );
}
