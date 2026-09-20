# -*- coding: utf-8 -*-
"""
Concept Solver Module for Math Mitra (10th SSC AP & TS)
Answers conceptual, definition, and theoretical questions such as:
- 'What is an Arithmetic Progression'
- 'Define quadratic equation'
- 'What is Euclid's Division Lemma'
- 'State Pythagoras theorem'
- 'What is trigonometry'
Provides bilingual (English and Telugu) textbook definitions, standard forms,
formulas, solved examples, and SSC Board exam tips.
"""

import re
from typing import Optional, Dict, Any

CONCEPT_TOPICS = [
    # 1. ARITHMETIC PROGRESSION (AP)
    {
        "id": "ap",
        "chapter_id": 6,
        "chapter_en": "Progressions (Arithmetic Progression)",
        "chapter_te": "శ్రేఢులు (అంకశ్రేఢి)",
        "keywords": [
            r'\barithmetic\s+progression\b',
            r'\bap\b',
            r'అంక\s*శ్రేఢి',
            r'\bcommon\s+difference\b',
            r'సామాన్య\s*భేదం'
        ],
        "formulas": [
            "a_n = a + (n - 1)d",
            "S_n = \\frac{n}{2}[2a + (n - 1)d] = \\frac{n}{2}[a + l]",
            "d = a_{k+1} - a_k"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
An **Arithmetic Progression (AP)** is a sequence of numbers in which each term is obtained by adding a fixed number to the preceding term, except the first term.

• **First Term ($a$ or $a_1$):** The starting number of the sequence.  
• **Common Difference ($d$):** The fixed number added to each successive term ($d = a_{k+1} - a_k$). The common difference can be **positive, negative, or zero**.

---

### 📐 Standard Form of an AP
$$a, \\; a + d, \\; a + 2d, \\; a + 3d, \\; \\dots, \\; a + (n - 1)d$$

---

### 🔑 Key Formulas to Remember

1. **$n^{\\text{th}}$ Term (General Term) Formula:**
$$a_n = a + (n - 1)d$$
*(Use this formula to find any specific term, such as the 10th term or 20th term)*

2. **Sum of First $n$ Terms ($S_n$):**
$$S_n = \\frac{n}{2} \\left[ 2a + (n - 1)d \\right]$$
**Or, when the last term ($l$ or $a_n$) is known:**
$$S_n = \\frac{n}{2} (a + l)$$

3. **Common Difference Condition:**
$$d = a_2 - a_1 = a_3 - a_2 = a_4 - a_3 = \\dots$$

---

### 💡 Solved Textbook Example

**Example:** Given the sequence $2, 7, 12, 17, \\dots$  
1. **First term ($a$):** $a = 2$  
2. **Common difference ($d$):** $d = 7 - 2 = 5$  
3. **Find the $10^{\\text{th}}$ term ($a_{10}$):**
$$a_{10} = a + (10 - 1)d = 2 + 9(5) = 2 + 45 = 47$$

4. **Sum of first $10$ terms ($S_{10}$):**
$$S_{10} = \\frac{10}{2} [2(2) + (10 - 1)(5)] = 5 [4 + 45] = 5 \\times 49 = 245$$

---

### 🏆 SSC Board Exam Tip
In AP & TS 10th Class Board exams:
• Always state the formula $a_n = a + (n - 1)d$ before substituting numbers (1 mark allocated for formula).  
• To verify if a given sequence is an AP, check if $(a_2 - a_1) = (a_3 - a_2)$. If the differences are not equal, it is **not an AP**.
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
మొదటి పదం తప్ప మిగిలిన ప్రతి పదం దాని ముందు పదానికి ఒక స్థిర సంఖ్యను కలపడం ద్వారా ఏర్పడే సంఖ్యల జాబితాను **అంకశ్రేఢి (Arithmetic Progression - AP)** అంటారు.

• **మొదటి పదం ($a$):** శ్రేఢిలోని ప్రారంభ సంఖ్య.  
• **సామాన్య భేదం ($d$):** ప్రతి పదానికి కలిపే స్థిర సంఖ్య ($d = a_{k+1} - a_k$). ఇది **ధనాత్మకం, రుణాత్మకం లేదా సున్నా** కావచ్చు.

---

### 📐 అంకశ్రేఢి సాధారణ రూపం
$$a, \\; a + d, \\; a + 2d, \\; a + 3d, \\; \\dots, \\; a + (n - 1)d$$

---

### 🔑 ముఖ్యమైన సూత్రాలు

1. **$n$ వ పదం (సాధారణ పదం) సూత్రం:**
$$a_n = a + (n - 1)d$$

2. **మొదటి $n$ పదాల మొత్తం ($S_n$):**
$$S_n = \\frac{n}{2} \\left[ 2a + (n - 1)d \\right]$$
**చివరి పదం ($l$) తెలిసినప్పుడు:**
$$S_n = \\frac{n}{2} (a + l)$$

3. **సామాన్య భేదం నియమం:**
$$d = a_2 - a_1 = a_3 - a_2 = a_4 - a_3 = \\dots$$

---

### 💡 ఉదాహరణ లెక్క

**ఉదాహరణ:** $2, 7, 12, 17, \\dots$ శ్రేఢిలో:  
1. **మొదటి పదం ($a$):** $a = 2$  
2. **సామాన్య భేదం ($d$):** $d = 7 - 2 = 5$  
3. **10వ పదం ($a_{10}$):**
$$a_{10} = a + (10 - 1)d = 2 + 9(5) = 2 + 45 = 47$$

4. **మొదటి 10 పదాల మొత్తం ($S_{10}$):**
$$S_{10} = \\frac{10}{2} [2(2) + (10 - 1)5] = 5 [4 + 45] = 5 \\times 49 = 245$$

---

### 🏆 బోర్డు పరీక్ష ముఖ్యమైన చిట్కా
బోర్డు పరీక్షల్లో అంకశ్రేఢి నుండి $a_n$ లేదా $S_n$ కనుగొనే లెక్కలు 2 మార్కులు మరియు 4 మార్కులలో వస్తాయి. లెక్క చేసేటప్పుడు ముందుగా సూత్రం తప్పక రాయాలి.
"""
    },

    # 2. GEOMETRIC PROGRESSION (GP)
    {
        "id": "gp",
        "chapter_id": 6,
        "chapter_en": "Progressions (Geometric Progression)",
        "chapter_te": "శ్రేఢులు (గుణశ్రేఢి)",
        "keywords": [
            r'\bgeometric\s+progression\b',
            r'\bgp\b',
            r'గుణ\s*శ్రేఢి',
            r'\bcommon\s+ratio\b',
            r'సామాన్య\s*నిష్పత్తి'
        ],
        "formulas": [
            "a_n = a \\cdot r^{n-1}",
            "r = \\frac{a_{k+1}}{a_k}",
            "S_n = \\frac{a(r^n - 1)}{r - 1}"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
A **Geometric Progression (GP)** is a sequence of non-zero numbers where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the **common ratio ($r$)**.

• **First Term ($a$):** The first number in the sequence.  
• **Common Ratio ($r$):** The ratio of any term to its preceding term ($r = \\frac{a_{k+1}}{a_k}$).

---

### 📐 Standard Form of a GP
$$a, \\; ar, \\; ar^2, \\; ar^3, \\; \\dots, \\; ar^{n-1}$$

---

### 🔑 Key Formulas
1. **$n^{\\text{th}}$ Term of a GP:**
$$a_n = a \\cdot r^{n-1}$$

2. **Common Ratio ($r$):**
$$r = \\frac{a_2}{a_1} = \\frac{a_3}{a_2} = \\dots$$

3. **Sum of First $n$ Terms ($S_n$):**
$$S_n = \\frac{a(r^n - 1)}{r - 1} \\quad (r > 1) \\qquad \\text{or} \\qquad S_n = \\frac{a(1 - r^n)}{1 - r} \\quad (r < 1)$$

---

### 💡 Solved Example
Given GP: $3, 6, 12, 24, \\dots$  
• First term $a = 3$, Common ratio $r = \\frac{6}{3} = 2$  
• $6^{\\text{th}}$ term: $a_6 = 3 \\times 2^{6-1} = 3 \\times 2^5 = 3 \\times 32 = 96$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
మొదటి పదం తప్ప మిగిలిన ప్రతి పదం దాని ముందు పదాన్ని ఒక స్థిర సంఖ్యతో గుణించడం ద్వారా ఏర్పడే శ్రేఢిని **గుణశ్రేఢి (Geometric Progression - GP)** అంటారు.

• **మొదటి పదం ($a$):** ప్రారంభ సంఖ్య.  
• **సామాన్య నిష్పత్తి ($r$):** ప్రతి పదం మరియు దాని మునుపటి పదాల నిష్పత్తి ($r = \\frac{a_{k+1}}{a_k}$).

---

### 📐 గుణశ్రేఢి సాధారణ రూపం
$$a, \\; ar, \\; ar^2, \\; ar^3, \\; \\dots, \\; ar^{n-1}$$

---

### 🔑 ముఖ్యమైన సూత్రాలు
1. **$n$ వ పదం సూత్రం:** $a_n = a \\cdot r^{n-1}$  
2. **సామాన్య నిష్పత్తి:** $r = \\frac{a_2}{a_1} = \\frac{a_3}{a_2}$  
3. **మొదటి $n$ పదాల మొత్తం:** $S_n = \\frac{a(r^n - 1)}{r - 1}$
"""
    },

    # 3. EUCLID'S DIVISION LEMMA / ALGORITHM
    {
        "id": "euclid",
        "chapter_id": 1,
        "chapter_en": "Real Numbers (Euclid's Division Lemma)",
        "chapter_te": "వాస్తవ సంఖ్యలు (యూక్లిడ్ భాగహార న్యాయం)",
        "keywords": [
            r'euclid',
            r'division\s+lemma',
            r'division\s+algorithm',
            r'యూక్లిడ్',
            r'భాగహార\s*న్యాయం'
        ],
        "formulas": [
            "a = bq + r \\quad (0 \\le r < b)",
            "\\text{Dividend} = \\text{Divisor} \\times \\text{Quotient} + \\text{Remainder}"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Statement of Euclid's Division Lemma
Given two positive integers $a$ and $b$, there exist unique whole numbers $q$ (quotient) and $r$ (remainder) satisfying:
$$a = bq + r, \\quad \\text{where } 0 \\le r < b$$

• **$a$:** Dividend  
• **$b$:** Divisor  
• **$q$:** Quotient  
• **$r$:** Remainder (must always be $\\ge 0$ and strictly less than $b$)

---

### 📐 Euclid's Division Algorithm for HCF
To find the HCF of two positive integers $c$ and $d$ with $c > d$:
1. Apply Euclid's division lemma to find $q$ and $r$: $c = dq + r$.
2. If $r = 0$, then $d$ is the **HCF**.
3. If $r \\neq 0$, apply the division lemma to $d$ and $r$.
4. Continue the process until the remainder becomes $0$. The divisor at that final stage is $\\text{HCF}(c, d)$.

---

### 💡 Solved Example: Find HCF of 900 and 270
1. $900 = 270 \\times 3 + 90$  
2. $270 = 90 \\times 3 + 0$  
Since remainder is now $0$, the divisor is **$90$**.  
$$\\mathbf{\\text{HCF}(900, 270) = 90}$$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 యూక్లిడ్ భాగహార న్యాయం నిర్వచనం
ఏవైనా రెండు ధన పూర్ణ సంఖ్యలు $a, b$ లకు, కింది సంబంధాన్ని తృప్తిపరిచే ఏకైక పూర్ణ సంఖ్యల జత $q, r$ లు వ్యవస్థితమవుతాయి:
$$a = bq + r, \\quad \\text{ఇక్కడ } 0 \\le r < b$$

• **విభాజ్యం ($a$) = విభాజకం ($b$) $\\times$ భాగఫలం ($q$) + శేషం ($r$)**  
• శేషం $r$ ఎల్లప్పుడూ $0$ లేదా అంతకంటే ఎక్కువ మరియు విభాజకం $b$ కంటే తక్కువగా ఉండాలి.
"""
    },

    # 4. QUADRATIC EQUATIONS
    {
        "id": "quadratic",
        "chapter_id": 5,
        "chapter_en": "Quadratic Equations",
        "chapter_te": "వర్గ సమీకరణాలు",
        "keywords": [
            r'quadratic\s+equation',
            r'quadratic\s+formula',
            r'discriminant',
            r'nature\s+of\s+roots',
            r'వర్గ\s*సమీకరణ',
            r'విచక్షణి'
        ],
        "formulas": [
            "ax^2 + bx + c = 0 \\quad (a \\neq 0)",
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
            "D = b^2 - 4ac"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
A **Quadratic Equation** in the variable $x$ is an algebraic equation of the second degree.

---

### 📐 Standard Form
$$ax^2 + bx + c = 0, \\quad \\text{where } a, b, c \\in \\mathbb{R} \\text{ and } a \\neq 0$$

---

### 🔑 The Quadratic Formula (Sridharacharya's Rule)
The roots of the equation $ax^2 + bx + c = 0$ are given by:
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$

---

### 🔍 Discriminant ($D$) & Nature of Roots
The expression $D = b^2 - 4ac$ is called the **Discriminant**:
1. **If $D > 0$:** Two distinct real roots ($x_1 \\neq x_2$).  
2. **If $D = 0$:** Two equal real roots ($x = -\\frac{b}{2a}$).  
3. **If $D < 0$:** No real roots (roots are imaginary/complex).
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
చరరాశి యొక్క గరిష్ట ఘాతం 2 గా గల సమీకరణాన్ని **వర్గ సమీకరణం (Quadratic Equation)** అంటారు.

---

### 📐 వర్గ సమీకరణ ప్రమాణ రూపం
$$ax^2 + bx + c = 0, \\quad (a \\neq 0)$$

---

### 🔑 వర్గ సూత్రం (శ్రీధరాచార్య సూత్రం)
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$

---

### 🔍 విచక్షణి ($D$) మరియు మూలాల స్వభావం:
$D = b^2 - 4ac$ ను విచక్షణి అంటారు:
1. **$D > 0$ అయితే:** మూలాలు వాస్తవాలు మరియు అసమానాలు.  
2. **$D = 0$ అయితే:** మూలాలు వాస్తవాలు మరియు సమానాలు ($x = -\\frac{b}{2a}$).  
3. **$D < 0$ అయితే:** వాస్తవ మూలాలు ఉండవు.
"""
    },

    # 5. POLYNOMIALS & ZEROES
    {
        "id": "polynomial",
        "chapter_id": 3,
        "chapter_en": "Polynomials",
        "chapter_te": "బహుపదులు",
        "keywords": [
            r'\bpolynomials?\b',
            r'\bdegree\s+of\s+polynomial\b',
            r'\bzeroes?\s+of\s+polynomial\b',
            r'బహుపది',
            r'బహుపదులు',
            r'శూన్యాలు'
        ],
        "formulas": [
            "p(x) = a_n x^n + a_{n-1} x^{n-1} + \\dots + a_0",
            "\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha\\beta = \\frac{c}{a}",
            "p(x) = k[x^2 - (\\alpha + \\beta)x + \\alpha\\beta]"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
A **Polynomial** $p(x)$ in one variable $x$ is an algebraic expression of the form:
$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \\dots + a_1 x + a_0$$
where $a_n \\neq 0$ and the exponents $n, n-1, \\dots$ are **non-negative integers**.

• **Degree of Polynomial:** The highest power of $x$ with a non-zero coefficient.  
  - Degree 1: Linear Polynomial ($ax + b$)  
  - Degree 2: Quadratic Polynomial ($ax^2 + bx + c$)  
  - Degree 3: Cubic Polynomial ($ax^3 + bx^2 + cx + d$)

• **Zero of a Polynomial:** A real number $k$ is a zero of $p(x)$ if $p(k) = 0$.

---

### 🔑 Relationship between Zeroes and Coefficients (Quadratic $ax^2 + bx + c$)
If $\\alpha$ and $\\beta$ are the zeroes:
$$\\text{Sum of zeroes: } \\alpha + \\beta = -\\frac{b}{a}$$
$$\\text{Product of zeroes: } \\alpha\\beta = \\frac{c}{a}$$

• **Forming a Quadratic Polynomial when zeroes $\\alpha, \\beta$ are given:**
$$p(x) = k \\left[ x^2 - (\\alpha + \\beta)x + \\alpha\\beta \\right]$$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
చరరాశి యొక్క ఘాతాలు రుణేతర పూర్ణసంఖ్యలుగా గల బీజీయ సమాసాన్ని **బహుపది (Polynomial)** అంటారు.

• **వర్గ బహుపది ($ax^2 + bx + c$) శూన్యాలు $\\alpha, \\beta$ అయితే:**
$$\\text{శూన్యాల మొత్తం: } \\alpha + \\beta = -\\frac{b}{a}$$
$$\\text{శూన్యాల లబ్దం: } \\alpha\\beta = \\frac{c}{a}$$
"""
    },

    # 6. TRIGONOMETRY
    {
        "id": "trigonometry",
        "chapter_id": 11,
        "chapter_en": "Trigonometry",
        "chapter_te": "త్రికోణమితి",
        "keywords": [
            r'trigonometry',
            r'trigonometric\s+ratios',
            r'trigonometric\s+identities',
            r'త్రికోణమితి',
            r'సర్వసమీకరణాలు'
        ],
        "formulas": [
            "\\sin^2\\theta + \\cos^2\\theta = 1",
            "\\sec^2\\theta - \\tan^2\\theta = 1",
            "\\csc^2\\theta - \\cot^2\\theta = 1"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
**Trigonometry** is the branch of mathematics that studies relationships between the side lengths and angles of triangles, particularly right-angled triangles.

---

### 📐 The 6 Trigonometric Ratios (in Right $\\triangle ABC$)
• $\\sin \\theta = \\frac{\\text{Opposite Side}}{\\text{Hypotenuse}}$  
• $\\cos \\theta = \\frac{\\text{Adjacent Side}}{\\text{Hypotenuse}}$  
• $\\tan \\theta = \\frac{\\text{Opposite Side}}{\\text{Adjacent Side}} = \\frac{\\sin \\theta}{\\cos \\theta}$  
• $\\csc \\theta = \\frac{1}{\\sin \\theta}, \\quad \\sec \\theta = \\frac{1}{\\cos \\theta}, \\quad \\cot \\theta = \\frac{1}{\\tan \\theta}$

---

### 🔑 Fundamental Trigonometric Identities
1. $\\mathbf{\\sin^2\\theta + \\cos^2\\theta = 1}$  
2. $\\mathbf{\\sec^2\\theta - \\tan^2\\theta = 1} \\implies \\sec^2\\theta = 1 + \\tan^2\\theta$  
3. $\\mathbf{\\csc^2\\theta - \\cot^2\\theta = 1} \\implies \\csc^2\\theta = 1 + \\cot^2\\theta$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
లంబకోణ త్రిభుజంలోని భుజాల పొడవులు మరియు కోణాల మధ్య గల సంబంధాలను అధ్యయనం చేసే గణిత విభాగాన్ని **త్రికోణమితి (Trigonometry)** అంటారు.

---

### 🔑 ముఖ్యమైన త్రికోణమితి సర్వసమీకరణాలు
1. $\\sin^2\\theta + \\cos^2\\theta = 1$  
2. $\\sec^2\\theta - \\tan^2\\theta = 1$  
3. $\\csc^2\\theta - \\cot^2\\theta = 1$
"""
    },

    # 7. COORDINATE GEOMETRY
    {
        "id": "coordinate_geometry",
        "chapter_id": 7,
        "chapter_en": "Coordinate Geometry",
        "chapter_te": "నిరూపక రేఖాగణితం",
        "keywords": [
            r'coordinate\s+geometry',
            r'distance\s+formula',
            r'section\s+formula',
            r'centroid',
            r'నిరూపక\s*రేఖాగణితం',
            r'మధ్యబిందువు'
        ],
        "formulas": [
            "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
            "P(x, y) = \\left(\\frac{m_1x_2 + m_2x_1}{m_1+m_2}, \\frac{m_1y_2 + m_2y_1}{m_1+m_2}\\right)",
            "G = \\left(\\frac{x_1+x_2+x_3}{3}, \\frac{y_1+y_2+y_3}{3}\\right)"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
**Coordinate Geometry** is a branch of mathematics where geometric figures are represented and analyzed on a Cartesian plane using ordered pairs of real numbers $(x, y)$.

---

### 🔑 Essential Coordinate Geometry Formulas

1. **Distance between $(x_1, y_1)$ and $(x_2, y_2)$:**
$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

2. **Distance from Origin $(0, 0)$:**
$$d = \\sqrt{x^2 + y^2}$$

3. **Section Formula (Internal Division in ratio $m_1 : m_2$):**
$$P(x, y) = \\left( \\frac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\; \\frac{m_1y_2 + m_2y_1}{m_1 + m_2} \\right)$$

4. **Midpoint Formula:**
$$M = \\left( \\frac{x_1 + x_2}{2}, \\; \\frac{y_1 + y_2}{2} \\right)$$

5. **Centroid of a Triangle:**
$$G = \\left( \\frac{x_1 + x_2 + x_3}{3}, \\; \\frac{y_1 + y_2 + y_3}{3} \\right)$$

6. **Area of Triangle:**
$$\\Delta = \\frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
బిందువుల స్థానాలను క్రమయుగ్మాలు $(x, y)$ ద్వారా సూచిస్తూ జ్యామితీయ పటాల ధర్మాలను అధ్యయనం చేయడాన్ని **నిరూపక రేఖాగణితం** అంటారు.

---

### 🔑 ముఖ్యమైన సూత్రాలు
1. **రెండు బిందువుల మధ్య దూరం:** $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$  
2. **విభజన సూత్రం:** $P = \\left(\\frac{m_1x_2 + m_2x_1}{m_1+m_2}, \\frac{m_1y_2 + m_2y_1}{m_1+m_2}\\right)$  
3. **మధ్య బిందువు:** $M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)$  
4. **గురుత్వ కేంద్రం:** $G = \\left(\\frac{x_1+x_2+x_3}{3}, \\frac{y_1+y_2+y_3}{3}\\right)$
"""
    },

    # 8. SIMILAR TRIANGLES & THALES / PYTHAGORAS THEOREMS
    {
        "id": "similar_triangles",
        "chapter_id": 8,
        "chapter_en": "Similar Triangles",
        "chapter_te": "సరూప త్రిభుజాలు",
        "keywords": [
            r'similar\s+triangles?',
            r'thales\s+theorem',
            r'basic\s+proportionality\s+theorem',
            r'bpt',
            r'pythagoras\s+theorem',
            r'సరూప\s*త్రిభుజాలు',
            r'థేల్స్',
            r'పైథాగరస్'
        ],
        "formulas": [
            "\\frac{AD}{DB} = \\frac{AE}{EC} \\quad (\\text{Thales Theorem})",
            "AC^2 = AB^2 + BC^2 \\quad (\\text{Pythagoras Theorem})"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition of Similar Triangles
Two triangles are said to be **similar** (denoted by $\\sim$) if:
1. Their corresponding angles are **equal**.
2. Their corresponding sides are in the **same ratio (proportional)**.

---

### 📜 Core Board Exam Theorems

1. **Basic Proportionality Theorem (Thales Theorem):**
> If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, then the other two sides are divided in the same ratio:
$$\\frac{AD}{DB} = \\frac{AE}{EC}$$

2. **Pythagoras Theorem:**
> In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides:
$$(\\text{Hypotenuse})^2 = (\\text{Side}_1)^2 + (\\text{Side}_2)^2 \\implies AC^2 = AB^2 + BC^2$$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 సరూప త్రిభుజాల నిర్వచనం
రెండు త్రిభుజాల అనురూప కోణాలు సమానంగా ఉండి, వాటి అనురూప భుజాలు ఒకే నిష్పత్తిలో ఉంటే ఆ రెండు త్రిభుజాలను **సరూప త్రిభుజాలు** అంటారు.

---

### 📜 ముఖ్యమైన సిద్ధాంతాలు
1. **థేల్స్ సిద్ధాంతం (ప్రాథమిక అనుపాత సిద్ధాంతం):** $\\frac{AD}{DB} = \\frac{AE}{EC}$  
2. **పైథాగరస్ సిద్ధాంతం:** కర్ణము$^2$ = భుజము$^2$ + భుజము$^2$ ($AC^2 = AB^2 + BC^2$)
"""
    },

    # 9. SETS
    {
        "id": "sets",
        "chapter_id": 2,
        "chapter_en": "Sets",
        "chapter_te": "సమితులు",
        "keywords": [
            r'\bsets?\b',
            r'union\s+of\s+sets',
            r'intersection\s+of\s+sets',
            r'disjoint\s+sets',
            r'సమితి',
            r'సమితులు'
        ],
        "formulas": [
            "n(A \\cup B) = n(A) + n(B) - n(A \\cap B)",
            "A \\cup B = \\{x : x \\in A \\text{ or } x \\in B\\}",
            "A \\cap B = \\{x : x \\in A \\text{ and } x \\in B\\}"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition of a Set
A **Set** is a well-defined collection of distinct objects or elements. Sets are denoted by capital letters ($A, B, C$) and elements are enclosed in curly braces $\\{ \\}$.

---

### 🔑 Set Operations
• **Union ($A \\cup B$):** Elements belonging to $A$, or $B$, or both.  
• **Intersection ($A \\cap B$):** Elements belonging to both $A$ and $B$ (common elements).  
• **Difference ($A - B$):** Elements in $A$ that are not in $B$.  
• **Disjoint Sets:** If $A \\cap B = \\emptyset$ (no common elements).

---

### 📐 Cardinality Formula
$$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$$
*(If $A$ and $B$ are disjoint: $n(A \\cup B) = n(A) + n(B)$)*
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 సమితి నిర్వచనం
సునిర్వచించబడిన విభిన్న వస్తువులు లేదా మూలకాల సమూహాన్ని **సమితి (Set)** అంటారు.

---

### 🔑 సమితి పరిక్రియలు
• **సమ్మేళనం ($A \\cup B$):** $A$ లేదా $B$ లేదా రెండింటిలోని మూలకాలు.  
• **ఛేదనం ($A \\cap B$):** $A$ మరియు $B$ రెండింటిలోనూ ఉండే ఉమ్మడి మూలకాలు.  
• **భేదం ($A - B$):** $A$ లో ఉండి $B$ లో లేని మూలకాలు.  
• **కార్డినల్ సంఖ్య సూత్రం:** $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$
"""
    },

    # 10. STATISTICS (MEAN, MEDIAN, MODE)
    {
        "id": "statistics",
        "chapter_id": 14,
        "chapter_en": "Statistics",
        "chapter_te": "సాంఖ్యక శాస్త్రం",
        "keywords": [
            r'statistics',
            r'\bmean\b',
            r'\bmedian\b',
            r'\bmode\b',
            r'సాంఖ్యక\s*శాస్త్రం',
            r'సగటు',
            r'బాహుళకం',
            r'మధ్యగతం'
        ],
        "formulas": [
            "\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}",
            "\\text{Mode} = l + \\left(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right)h",
            "\\text{Median} = l + \\left(\\frac{\\frac{n}{2} - cf}{f}\\right)h"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Measures of Central Tendency in Statistics
In SSC 10th Class, the three core measures of central tendency for grouped frequency distributions are:

1. **Mean (Average $\\bar{x}$):**
$$\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}$$

2. **Mode (Most frequent observation):**
$$\\text{Mode} = l + \\left( \\frac{f_1 - f_0}{2f_1 - f_0 - f_2} \\right) \\times h$$
• $l$: Lower boundary of modal class  
• $f_1$: Frequency of modal class  
• $f_0$: Frequency of class preceding modal class  
• $f_2$: Frequency of class succeeding modal class  
• $h$: Size of class interval

3. **Median (Middle-most value):**
$$\\text{Median} = l + \\left( \\frac{\\frac{n}{2} - cf}{f} \\right) \\times h$$
• $cf$: Cumulative frequency of class preceding median class  
• $f$: Frequency of median class
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 కేంద్రీయ ప్రవృత్తి మానాలు (సాంఖ్యక శాస్త్రం)
1. **సగటు (Mean):** $\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}$  
2. **బాహుళకం (Mode):** $\\text{Mode} = l + \\left(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right) \\times h$  
3. **మధ్యగతం (Median):** $\\text{Median} = l + \\left(\\frac{\\frac{n}{2} - cf}{f}\\right) \\times h$
"""
    },

    # 11. PROBABILITY
    {
        "id": "probability",
        "chapter_id": 13,
        "chapter_en": "Probability",
        "chapter_te": "సంభావ్యత",
        "keywords": [
            r'probability',
            r'సంభావ్యత',
            r'sure\s+event',
            r'impossible\s+event'
        ],
        "formulas": [
            "P(E) = \\frac{n(E)}{n(S)}",
            "0 \\le P(E) \\le 1",
            "P(E) + P(\\bar{E}) = 1"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 Definition
**Probability** is the measure of the likelihood or chance that a given event will occur.

---

### 🔑 Fundamental Formulas
$$P(E) = \\frac{\\text{Number of outcomes favourable to event } E}{\\text{Total number of possible outcomes in sample space } S} = \\frac{n(E)}{n(S)}$$

• **Probability Range:** $0 \\le P(E) \\le 1$  
• **Impossible Event:** $P(E) = 0$  
• **Sure / Certain Event:** $P(E) = 1$  
• **Complementary Event ($E$ and $\\bar{E}$):**
$$P(E) + P(\\bar{E}) = 1 \\implies P(\\bar{E}) = 1 - P(E)$$
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 నిర్వచనం
ఒక ఘటన జరగడానికి గల అవకాశాన్ని సంఖ్యాపరంగా తెలియజేసే మానాన్ని **సంభావ్యత (Probability)** అంటారు.

• **సూత్రం:** $P(E) = \\frac{\\text{ఘటన } E \\text{ కు అనుకూల పర్యవసానాల సంఖ్య}}{\\text{మొత్తం సాధ్యమయ్యే పర్యవసానాల సంఖ్య}} = \\frac{n(E)}{n(S)}$  
• సంభావ్యత విలువ ఎల్లప్పుడూ $0$ మరియు $1$ మధ్య ఉంటుంది ($0 \\le P(E) \\le 1$).  
• పూరక ఘటన నియమం: $P(E) + P(\\bar{E}) = 1$
"""
    },

    # 12. MENSURATION (SURFACE AREAS & VOLUMES)
    {
        "id": "mensuration",
        "chapter_id": 10,
        "chapter_en": "Mensuration",
        "chapter_te": "క్షేత్రమితి",
        "keywords": [
            r'mensuration',
            r'surface\s+area',
            r'volume\s+of',
            r'cylinder',
            r'cone',
            r'sphere',
            r'క్షేత్రమితి',
            r'ఘనపరిమాణం'
        ],
        "formulas": [
            "\\text{Cylinder: } \\text{CSA} = 2\\pi rh, \\; V = \\pi r^2 h",
            "\\text{Cone: } \\text{CSA} = \\pi rl, \\; V = \\frac{1}{3}\\pi r^2 h",
            "\\text{Sphere: } \\text{TSA} = 4\\pi r^2, \\; V = \\frac{4}{3}\\pi r^3"
        ],
        "en_text": """### 🧮 Question
**{query_text}**

---

### 📖 3D Mensuration Formula Guide

| Solid Shape | Curved Surface Area (CSA) | Total Surface Area (TSA) | Volume ($V$) |
| :--- | :--- | :--- | :--- |
| **Cylinder** | $2\\pi rh$ | $2\\pi r(r + h)$ | $\\pi r^2 h$ |
| **Cone** | $\\pi rl$ ($l = \\sqrt{r^2 + h^2}$) | $\\pi r(l + r)$ | $\\frac{1}{3}\\pi r^2 h$ |
| **Sphere** | $4\\pi r^2$ | $4\\pi r^2$ | $\\frac{4}{3}\\pi r^3$ |
| **Hemisphere** | $2\\pi r^2$ | $3\\pi r^2$ | $\\frac{2}{3}\\pi r^3$ |
| **Cuboid** | $2h(l + b)$ | $2(lb + bh + hl)$ | $l \\times b \\times h$ |
| **Cube** | $4a^2$ | $6a^2$ | $a^3$ |
""",
        "te_text": """### 🧮 ప్రశ్న
**{query_text}**

---

### 📖 క్షేత్రమితి ముఖ్య సూత్రాలు (ఘనపరిమాణాలు & వైశాల్యాలు)
• **స్తూపం (Cylinder):** ప్రక్కతల వైశాల్యం = $2\\pi rh$, ఘనపరిమాణం = $\\pi r^2 h$  
• **శంకువు (Cone):** ప్రక్కతల వైశాల్యం = $\\pi rl$, ఘనపరిమాణం = $\\frac{1}{3}\\pi r^2 h$  
• **గోళం (Sphere):** ఉపరితల వైశాల్యం = $4\\pi r^2$, ఘనపరిమాణం = $\\frac{4}{3}\\pi r^3$  
• **అర్ధగోళం (Hemisphere):** ప్రక్కతల వైశాల్యం = $2\\pi r^2$, సంపూర్ణతల వైశాల్యం = $3\\pi r^2$, ఘనపరిమాణం = $\\frac{2}{3}\\pi r^3$
"""
    }
]

# Words that strongly signal a conceptual or definition question
CONCEPT_QUERY_INDICATORS = [
    r'what\s+is',
    r'what\s+are',
    r'define',
    r'definition',
    r'explain',
    r'meaning\s+of',
    r'tell\s+me\s+about',
    r'state',
    r'how\s+to\s+define',
    r'formula\s+of',
    r'formulas?\s+for',
    r'rules?\s+of',
    r'notes?\s+on',
    r'properties\s+of',
    r'అంటే\s*ఏమిటి',
    r'అనగానేమి',
    r'నిర్వచించండి',
    r'సూత్రం',
    r'వివరించండి'
]

def solve_concept_query(query: str, lang: str = "en") -> Optional[Dict[str, Any]]:
    """
    Checks if query is a conceptual / definition question.
    Returns structured solution dict if matched, otherwise None.
    """
    if not query:
        return None

    norm = query.strip()
    q_low = norm.lower()

    # Check if this looks like a conceptual question or a raw topic name
    is_concept_indicator = any(re.search(pat, q_low) for pat in CONCEPT_QUERY_INDICATORS)
    has_math_equation = bool(re.search(r'=|\+|-|\*|/|\^|\b\d{2,}\b', q_low) and not is_concept_indicator)

    # If it's a direct calculation with numbers/equals without concept indicators, skip
    if has_math_equation and not is_concept_indicator:
        return None

    # Search through CONCEPT_TOPICS
    matched_topic = None
    for topic in CONCEPT_TOPICS:
        for kw in topic["keywords"]:
            if re.search(kw, q_low):
                matched_topic = topic
                break
        if matched_topic:
            break

    if not matched_topic:
        return None

    en_text = matched_topic["en_text"].replace("{query_text}", norm)
    te_text = matched_topic["te_text"].replace("{query_text}", norm)

    return {
        "query": query,
        "language": lang,
        "chapter_id": matched_topic["chapter_id"],
        "chapter_en": matched_topic["chapter_en"],
        "chapter_te": matched_topic["chapter_te"],
        "page_reference": f"Chapter {matched_topic['chapter_id']} (SCERT Class 10)",
        "exercise_reference": "Concept & Definition",
        "formulas": matched_topic["formulas"],
        "explanation": {
            "en": en_text,
            "te": te_text
        }
    }
