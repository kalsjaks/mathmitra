import { useEffect } from 'react';

/**
 * Updates document <title>, meta description, canonical link, and JSON-LD structured data.
 */
export default function SeoHead({ title, description, canonicalUrl, jsonLd }) {
  useEffect(() => {
    // 1. Update Title
    const prevTitle = document.title;
    if (title) {
      document.title = title;
    }

    // 2. Update Meta Description
    let metaDesc = document.querySelector('meta[name="description"]');
    const prevDesc = metaDesc ? metaDesc.getAttribute('content') : '';
    if (description) {
      if (!metaDesc) {
        metaDesc = document.createElement('meta');
        metaDesc.setAttribute('name', 'description');
        document.head.appendChild(metaDesc);
      }
      metaDesc.setAttribute('content', description);
    }

    // 3. Update OpenGraph Title & Description & URL
    let ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle && title) ogTitle.setAttribute('content', title);

    let ogDesc = document.querySelector('meta[property="og:description"]');
    if (ogDesc && description) ogDesc.setAttribute('content', description);

    let ogUrl = document.querySelector('meta[property="og:url"]');
    if (ogUrl && canonicalUrl) ogUrl.setAttribute('content', canonicalUrl);

    // 4. Update Canonical Link
    let canonical = document.querySelector('link[rel="canonical"]');
    if (!canonical && canonicalUrl) {
      canonical = document.createElement('link');
      canonical.setAttribute('rel', 'canonical');
      document.head.appendChild(canonical);
    }
    if (canonical && canonicalUrl) {
      canonical.setAttribute('href', canonicalUrl);
    }

    // 5. Injected JSON-LD Schema (e.g., FAQPage / LearningResource)
    let scriptTag = null;
    if (jsonLd) {
      scriptTag = document.createElement('script');
      scriptTag.type = 'application/ld+json';
      scriptTag.text = JSON.stringify(jsonLd);
      scriptTag.id = 'seo-json-ld';
      const existing = document.getElementById('seo-json-ld');
      if (existing) existing.remove();
      document.head.appendChild(scriptTag);
    }

    return () => {
      // Revert to original title/description on unmount if leaving SEO pages
      if (prevTitle) document.title = prevTitle;
      if (metaDesc && prevDesc) metaDesc.setAttribute('content', prevDesc);
      const existing = document.getElementById('seo-json-ld');
      if (existing) existing.remove();
    };
  }, [title, description, canonicalUrl, jsonLd]);

  return null;
}
