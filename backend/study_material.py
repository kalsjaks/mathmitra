# -*- coding: utf-8 -*-
"""
Study Material Repository for Math Mitra (10th SSC AP & TS)
Contains:
1. Complete formulas for all 14 chapters with LaTeX and Telugu translations
2. Exam Prep Mode: How to pass SSC Math with 40+ marks guarantee (high-yield chapters, 15 guaranteed questions, 5-day study plan)
3. Previous SSC Board Exam question papers (AP & TS 2019-2024)
4. Textbook question extractor
"""

import re
import json
import os

INDEX_PATH = os.path.join(os.path.dirname(__file__), "data", "textbook_index.json")

# =============================================================================
# 1. FORMULAS FOR ALL 14 CHAPTERS
# =============================================================================
CHAPTER_FORMULAS = [
    {
        "id": 1,
        "name_en": "Real Numbers",
        "name_te": "వాస్తవ సంఖ్యలు",
        "category": "Number Systems",
        "weightage": "6 - 8 Marks",
        "formulas": [
            {
                "title_en": "Euclid's Division Lemma",
                "title_te": "యూక్లిడ్ భాగహార న్యాయం",
                "latex": "a = bq + r \\quad (0 \\le r < b)",
                "note_en": "For any two positive integers a and b, there exist unique whole numbers q (quotient) and r (remainder).",
                "note_te": "a, b ధన పూర్ణ సంఖ్యలైతే, a = bq + r (0 <= r < b) అయ్యేటట్లు ఏకైక పూర్ణ సంఖ్యల జత q, r లు ఉంటాయి."
            },
            {
                "title_en": "Fundamental Theorem of Arithmetic (HCF & LCM)",
                "title_te": "అంకగణిత ప్రాథమిక సిద్ధాంతం",
                "latex": "\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b",
                "note_en": "Product of HCF and LCM of two numbers equals product of the numbers.",
                "note_te": "రెండు సంఖ్యల గ.సా.భా మరియు క.సా.గు ల లబ్దం = ఆ రెండు సంఖ్యల లబ్దం."
            },
            {
                "title_en": "Terminating Decimal Condition",
                "title_te": "అంతమయ్యే దశాంశం నియమం",
                "latex": "q = 2^n \\times 5^m \\quad (n, m \\ge 0)",
                "note_en": "Rational number p/q has terminating decimal expansion if denominator q has only 2 and 5 as prime factors.",
                "note_te": "హారం q అనేది 2^n * 5^m రూపంలో ఉంటే ఆ దశాంశం అంతమవుతుంది."
            },
            {
                "title_en": "Laws of Logarithms (All 5 Laws)",
                "title_te": "సంవర్గమాన నియమాలు",
                "latex": "\\begin{aligned} \\log_a (xy) &= \\log_a x + \\log_a y \\\\ \\log_a \\left(\\frac{x}{y}\\right) &= \\log_a x - \\log_a y \\\\ \\log_a (x^m) &= m \\log_a x \\\\ \\log_a a &= 1, \\quad \\log_a 1 = 0 \\\\ a^{\\log_a x} &= x \\end{aligned}",
                "note_en": "Essential for 2-mark and 4-mark questions in board exams.",
                "note_te": "బోర్డు పరీక్షల్లో 2 మరియు 4 మార్కుల ప్రశ్నలకు అత్యంత ముఖ్యం."
            }
        ],
        "mnemonic": "Remember: Product in log becomes Addition (log xy = log x + log y); Division becomes Subtraction!"
    },
    {
        "id": 2,
        "name_en": "Sets",
        "name_te": "సమితులు",
        "category": "Algebra & Foundations",
        "weightage": "6 Marks",
        "formulas": [
            {
                "title_en": "Cardinality of Union of Two Sets",
                "title_te": "రెండు సమితుల సమ్మేళనం కార్డినల్ సంఖ్య",
                "latex": "n(A \\cup B) = n(A) + n(B) - n(A \\cap B)",
                "note_en": "If A and B are disjoint sets (A ∩ B = ∅), then n(A ∪ B) = n(A) + n(B).",
                "note_te": "A, B లు వియుక్త సమితులైతే (A ∩ B = Φ), n(A ∪ B) = n(A) + n(B) అవుతుంది."
            },
            {
                "title_en": "Union of Sets",
                "title_te": "సమితుల సమ్మేళనం",
                "latex": "A \\cup B = \\{x : x \\in A \\text{ or } x \\in B\\}",
                "note_en": "Combines all elements of both sets without duplication.",
                "note_te": "రెండు సమితులలోని అన్ని మూలకాల సమాహారం."
            },
            {
                "title_en": "Intersection of Sets",
                "title_te": "సమితుల ఛేదనం",
                "latex": "A \\cap B = \\{x : x \\in A \\text{ and } x \\in B\\}",
                "note_en": "Common elements present in both sets.",
                "note_te": "రెండు సమితులలో ఉమ్మడిగా ఉండే మూలకాలు."
            },
            {
                "title_en": "Difference of Sets",
                "title_te": "సమితుల భేదం",
                "latex": "A - B = \\{x : x \\in A \\text{ and } x \\notin B\\}",
                "note_en": "Elements in A that are NOT in B.",
                "note_te": "A లో ఉండి B లో లేని మూలకాలు."
            }
        ],
        "mnemonic": "Venn Diagrams: Union is full coloring; Intersection is overlapping middle football; Difference A-B is only the left crescent!"
    },
    {
        "id": 3,
        "name_en": "Polynomials",
        "name_te": "బహుపదులు",
        "category": "Algebra",
        "weightage": "6 - 8 Marks",
        "formulas": [
            {
                "title_en": "Zero of Linear Polynomial",
                "title_te": "రేఖీయ బహుపది శూన్యం",
                "latex": "p(x) = ax + b \\implies x = -\\frac{b}{a}",
                "note_en": "Point of intersection with x-axis is (-b/a, 0).",
                "note_te": "X-అక్షాన్ని ఖండించే బిందువు (-b/a, 0)."
            },
            {
                "title_en": "Sum and Product of Zeroes (Quadratic)",
                "title_te": "వర్గ బహుపది శూన్యాల మొత్తం & లబ్దం",
                "latex": "\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha\\beta = \\frac{c}{a}",
                "note_en": "For quadratic polynomial p(x) = ax^2 + bx + c.",
                "note_te": "వర్గ బహుపది p(x) = ax^2 + bx + c కి."
            },
            {
                "title_en": "Quadratic Polynomial Formation",
                "title_te": "వర్గ బహుపదిని రూపొందించు సూత్రం",
                "latex": "p(x) = k\\left[x^2 - (\\alpha + \\beta)x + \\alpha\\beta\\right] \\quad (k \\ne 0)",
                "note_en": "Used when zeroes or their sum and product are given.",
                "note_te": "శూన్యాలు లేదా వాటి మొత్తం, లబ్దాలు ఇచ్చినప్పుడు వర్గ బహుపది రాయడానికి."
            },
            {
                "title_en": "Cubic Polynomial Relations",
                "title_te": "ఘన బహుపది శూన్యాల సంబంధాలు",
                "latex": "\\begin{aligned} \\alpha + \\beta + \\gamma &= -\\frac{b}{a} \\\\ \\alpha\\beta + \\beta\\gamma + \\gamma\\alpha &= \\frac{c}{a} \\\\ \\alpha\\beta\\gamma &= -\\frac{d}{a} \\end{aligned}",
                "note_en": "For cubic polynomial p(x) = ax^3 + bx^2 + cx + d.",
                "note_te": "ఘన బహుపది p(x) = ax^3 + bx^2 + cx + d కి."
            },
            {
                "title_en": "Division Algorithm for Polynomials",
                "title_te": "బహుపదుల భాగహార న్యాయం",
                "latex": "p(x) = g(x) \\cdot q(x) + r(x) \\quad (\\text{deg } r(x) < \\text{deg } g(x))",
                "note_en": "Dividend = Divisor * Quotient + Remainder.",
                "note_te": "విభాజ్యం = విభాజకం * భాగఫలం + శేషం."
            }
        ],
        "mnemonic": "Coefficients alternate signs: Sum of 1 zero at a time is -b/a; Sum of products of 2 is +c/a; Product of 3 is -d/a!"
    },
    {
        "id": 4,
        "name_en": "Pair of Linear Equations in Two Variables",
        "name_te": "రెండు చరరాశులలో రేఖీయ సమీకరణాల జత",
        "category": "Algebra",
        "weightage": "6 - 8 Marks",
        "formulas": [
            {
                "title_en": "Consistency & Number of Solutions (Table)",
                "title_te": "సంగత మరియు అసంగత సమీకరణాల నిబంధనలు",
                "latex": "\\begin{aligned} \\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2} &\\implies \\text{Intersecting Lines (Unique Solution / Consistent)} \\\\ \\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} &\\implies \\text{Coincident Lines (Infinitely Many Solutions / Dependent)} \\\\ \\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2} &\\implies \\text{Parallel Lines (No Solution / Inconsistent)} \\end{aligned}",
                "note_en": "GUARANTEED 1-mark or 2-mark question in every SSC board paper!",
                "note_te": "ప్రతి బోర్డు పరీక్షలో గ్యారెంటీగా అడిగే 1 లేదా 2 మార్కుల ప్రశ్న!"
            }
        ],
        "mnemonic": "If slopes differ (a1/a2 != b1/b2), they cross ONCE. If everything equals, they lie ON TOP. If only constants differ, they never meet (PARALLEL)."
    },
    {
        "id": 5,
        "name_en": "Quadratic Equations",
        "name_te": "వర్గ సమీకరణాలు",
        "category": "Algebra",
        "weightage": "8 Marks",
        "formulas": [
            {
                "title_en": "Standard Form & Quadratic Formula",
                "title_te": "ప్రామాణిక రూపం & వర్గ సమీకరణ సూత్రం",
                "latex": "ax^2 + bx + c = 0 \\implies x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
                "note_en": "Discovered by Indian mathematician Sridharacharya.",
                "note_te": "శ్రీధరాచార్య వర్గ సమీకరణ సూత్రం."
            },
            {
                "title_en": "Discriminant & Nature of Roots (Delta)",
                "title_te": "విచక్షణి మరియు మూలాల స్వభావం",
                "latex": "\\begin{aligned} \\Delta = b^2 - 4ac > 0 &\\implies \\text{Two distinct real roots} \\\\ \\Delta = b^2 - 4ac = 0 &\\implies \\text{Two equal real roots } \\left(x = -\\frac{b}{2a}\\right) \\\\ \\Delta = b^2 - 4ac < 0 &\\implies \\text{No real roots (imaginary)} \\end{aligned}",
                "note_en": "If roots are equal, b^2 = 4ac (frequently asked to find unknown k).",
                "note_te": "మూలాలు సమానమైతే b^2 = 4ac అవుతుంది (k విలువ కనుగొనే లెక్కలు బోర్డు పరీక్షల్లో తరచూ వస్తాయి)."
            }
        ],
        "mnemonic": "Discriminant Delta decides destiny: Positive = 2 different roots, Zero = Twin equal roots, Negative = No real roots!"
    },
    {
        "id": 6,
        "name_en": "Progressions",
        "name_te": "శ్రేఢులు",
        "category": "Algebra",
        "weightage": "6 - 8 Marks",
        "formulas": [
            {
                "title_en": "n-th Term of an Arithmetic Progression (AP)",
                "title_te": "అంకశ్రేఢి లో nవ పదం (a_n)",
                "latex": "a_n = a + (n - 1)d",
                "note_en": "Where a = first term, d = common difference (a_2 - a_1), n = number of terms.",
                "note_te": "ఇక్కడ a = మొదటి పదం, d = సామాన్య భేదం (a_2 - a_1), n = పదాల సంఖ్య."
            },
            {
                "title_en": "Sum of First n Terms of AP (S_n)",
                "title_te": "అంకశ్రేఢి మొదటి n పదాల మొత్తం (S_n)",
                "latex": "S_n = \\frac{n}{2}[2a + (n - 1)d] = \\frac{n}{2}[a + l]",
                "note_en": "Use n/2 * (a + l) when the last term l is known.",
                "note_te": "చివరి పదం l తెలిసినప్పుడు S_n = n/2(a + l) ఉపయోగించండి."
            },
            {
                "title_en": "Geometric Progression (GP) n-th Term & Common Ratio",
                "title_te": "గుణశ్రేఢి nవ పదం (a_n) & సామాన్య నిష్పత్తి",
                "latex": "a_n = ar^{n-1}, \\quad r = \\frac{a_2}{a_1}",
                "note_en": "Where a = first term, r = common ratio.",
                "note_te": "ఇక్కడ a = మొదటి పదం, r = సామాన్య నిష్పత్తి (a_2 / a_1)."
            }
        ],
        "mnemonic": "AP adds difference d each time: a + (n-1)d. GP multiplies ratio r each time: a * r^(n-1)."
    },
    {
        "id": 7,
        "name_en": "Coordinate Geometry",
        "name_te": "నిరూపక జ్యామితి",
        "category": "Geometry & Algebra",
        "weightage": "8 Marks",
        "formulas": [
            {
                "title_en": "Distance Formula",
                "title_te": "రెండు బిందువుల మధ్య దూరం",
                "latex": "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
                "note_en": "Distance of point (x, y) from origin (0, 0) is sqrt(x^2 + y^2).",
                "note_te": "మూలబిందువు (0, 0) నుండి (x, y) బిందువుకు దూరం = √(x^2 + y^2)."
            },
            {
                "title_en": "Section Formula (Internal Division)",
                "title_te": "బిందు విభజన సూత్రం",
                "latex": "P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\; \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)",
                "note_en": "Divides line segment joining (x1, y1) and (x2, y2) in ratio m1 : m2.",
                "note_te": "రేఖాఖండాన్ని m1 : m2 నిష్పత్తిలో విభజించే బిందువు."
            },
            {
                "title_en": "Midpoint Formula",
                "title_te": "మధ్య బిందువు సూత్రం",
                "latex": "M = \\left( \\frac{x_1 + x_2}{2}, \\; \\frac{y_1 + y_2}{2} \\right)",
                "note_en": "Special case of section formula where m1 : m2 = 1 : 1.",
                "note_te": "m1 : m2 = 1 : 1 అయినప్పుడు మధ్య బిందువు."
            },
            {
                "title_en": "Centroid of a Triangle",
                "title_te": "త్రిభుజ గురుత్వ కేంద్రం (G)",
                "latex": "G = \\left( \\frac{x_1 + x_2 + x_3}{3}, \\; \\frac{y_1 + y_2 + y_3}{3} \\right)",
                "note_en": "Point of concurrency of the three medians of the triangle.",
                "note_te": "త్రిభుజ మధ్యగత రేఖల సంగమ బిందువు."
            },
            {
                "title_en": "Area of a Triangle & Collinearity",
                "title_te": "త్రిభుజ వైశాల్యం మరియు సరేఖీయత",
                "latex": "\\Delta = \\frac{1}{2} \\left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \\right|",
                "note_en": "If Area = 0, the three points are Collinear (lie on the same straight line)!",
                "note_te": "వైశాల్యం = 0 అయితే, ఆ మూడు బిందువులు సరేఖీయాలు (ఒకే సరళరేఖపై ఉంటాయి)!"
            }
        ],
        "mnemonic": "Triangle Area cycle: 1(2-3) + 2(3-1) + 3(1-2). Notice the cyclic indices 1 -> 2 -> 3 -> 1!"
    },
    {
        "id": 8,
        "name_en": "Similar Triangles",
        "name_te": "సరూప త్రిభుజాలు",
        "category": "Geometry",
        "weightage": "8 Marks",
        "formulas": [
            {
                "title_en": "Basic Proportionality Theorem (Thales Theorem)",
                "title_te": "ప్రాథమిక అనుపాత సిద్ధాంతం (థేల్స్ సిద్ధాంతం)",
                "latex": "\\text{In } \\Delta ABC, \\; DE \\parallel BC \\implies \\frac{AD}{DB} = \\frac{AE}{EC}",
                "note_en": "A line drawn parallel to one side divides the other two sides in the same ratio.",
                "note_te": "ఒక భుజానికి సమాంతరంగా గీసిన సరళరేఖ మిగిలిన రెండు భుజాలను సమాన నిష్పత్తిలో విభజిస్తుంది."
            },
            {
                "title_en": "Ratio of Areas of Similar Triangles",
                "title_te": "సరూప త్రిభుజాల వైశాల్యాల నిష్పత్తి",
                "latex": "\\frac{\\text{Area}(\\Delta ABC)}{\\text{Area}(\\Delta PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{AC}{PR}\\right)^2",
                "note_en": "Ratio of areas equals the ratio of squares of corresponding sides.",
                "note_te": "వైశాల్యాల నిష్పత్తి వాటి అనురూప భుజాల వర్గాల నిష్పత్తికి సమానం."
            },
            {
                "title_en": "Baudhayan / Pythagoras Theorem",
                "title_te": "పైథాగరస్ సిద్ధాంతం (బౌద్ధాయన సిద్ధాంతం)",
                "latex": "\\text{In a right triangle: } (\\text{Hypotenuse})^2 = (\\text{Side}_1)^2 + (\\text{Side}_2)^2",
                "note_en": "In right triangle ABC right angled at B: AC^2 = AB^2 + BC^2.",
                "note_te": "లంబకోణ త్రిభుజంలో: కర్ణము^2 = భుజము^2 + భుజము^2."
            }
        ],
        "mnemonic": "BPT is the key to 4 and 8 marks! Remember: Parallel line = Proportional segments."
    },
    {
        "id": 9,
        "name_en": "Tangents and Secants to a Circle",
        "name_te": "వృత్తానికి స్పర్శరేఖలు మరియు ఛేదనరేఖలు",
        "category": "Geometry",
        "weightage": "6 Marks",
        "formulas": [
            {
                "title_en": "Radius and Tangent Perpendicularity",
                "title_te": "స్పర్శరేఖ మరియు వ్యాసార్థం లంబం",
                "latex": "OP \\perp PT \\quad (\\angle OPT = 90^\\circ)",
                "note_en": "The tangent at any point of a circle is perpendicular to the radius through the point of contact.",
                "note_te": "స్పర్శ బిందువు వద్ద గీసిన వ్యాసార్థం ఆ స్పర్శరేఖకు లంబంగా ఉంటుంది."
            },
            {
                "title_en": "Lengths of Tangents from External Point",
                "title_te": "బాహ్య బిందువు నుండి స్పర్శరేఖల పొడవులు",
                "latex": "PA = PB, \\quad PA = \\sqrt{d^2 - r^2}",
                "note_en": "Tangents drawn from an external point to a circle are equal in length.",
                "note_te": "బాహ్య బిందువు నుండి వృత్తానికి గీసిన స్పర్శరేఖల పొడవులు సమానం."
            },
            {
                "title_en": "Area of Segment of a Circle",
                "title_te": "వృత్త ఖండ వైశాల్యం",
                "latex": "\\text{Area of Sector} = \\frac{x^\\circ}{360^\\circ} \\times \\pi r^2, \\quad \\text{Length of Arc} = \\frac{x^\\circ}{360^\\circ} \\times 2\\pi r",
                "note_en": "Where x is the sector angle in degrees.",
                "note_te": "ఇక్కడ x అనేది సెక్టార్ కోణం (డిగ్రీలలో)."
            }
        ],
        "mnemonic": "A tangent kisses the circle at exactly 1 point and creates a 90-degree angle with the center's radius!"
    },
    {
        "id": 10,
        "name_en": "Mensuration",
        "name_te": "క్షేత్రమితి",
        "category": "Geometry & Measurement",
        "weightage": "8 - 10 Marks",
        "formulas": [
            {
                "title_en": "Right Circular Cylinder",
                "title_te": "స్తూపం (Cylinder)",
                "latex": "\\begin{aligned} \\text{Curved Surface Area (CSA)} &= 2\\pi rh \\\\ \\text{Total Surface Area (TSA)} &= 2\\pi r(h + r) \\\\ \\text{Volume (V)} &= \\pi r^2 h \\end{aligned}",
                "note_en": "Where r is radius, h is height.",
                "note_te": "r = వ్యాసార్థం, h = ఎత్తు."
            },
            {
                "title_en": "Right Circular Cone",
                "title_te": "శంఖువు (Cone)",
                "latex": "\\begin{aligned} \\text{Slant Height } l &= \\sqrt{r^2 + h^2} \\\\ \\text{CSA} &= \\pi rl \\\\ \\text{TSA} &= \\pi r(l + r) \\\\ \\text{Volume} &= \\frac{1}{3}\\pi r^2 h \\end{aligned}",
                "note_en": "Notice cone volume is exactly 1/3rd of the cylinder volume!",
                "note_te": "శంఖువు ఘనపరిమాణం స్తూప ఘనపరిమాణంలో 1/3 వ వంతు!"
            },
            {
                "title_en": "Sphere & Hemisphere",
                "title_te": "గోళం & అర్ధగోళం",
                "latex": "\\begin{aligned} \\text{Sphere: Surface Area} &= 4\\pi r^2, \\quad \\text{Volume} = \\frac{4}{3}\\pi r^3 \\\\ \\text{Hemisphere: CSA} &= 2\\pi r^2, \\quad \\text{TSA} = 3\\pi r^2, \\quad \\text{Volume} = \\frac{2}{3}\\pi r^3 \\end{aligned}",
                "note_en": "Crucial: Hemisphere TSA has 3pi*r^2 because of the flat circular base!",
                "note_te": "అర్ధగోళ సంపూర్ణతల వైశాల్యం = 3πr^2 (వక్రతలం 2πr^2 + వృత్తాకార అడుగుభాగం πr^2)."
            }
        ],
        "mnemonic": "Volume of Cone = 1/3 Cylinder; Volume of Hemisphere = 2/3 pi*r^3; Sphere = 4/3 pi*r^3!"
    },
    {
        "id": 11,
        "name_en": "Trigonometry",
        "name_te": "త్రికోణమితి",
        "category": "Trigonometry",
        "weightage": "8 - 10 Marks",
        "formulas": [
            {
                "title_en": "6 Trigonometric Ratios",
                "title_te": "6 త్రికోణమితి నిష్పత్తులు",
                "latex": "\\begin{aligned} \\sin \\theta &= \\frac{\\text{Opposite}}{\\text{Hypotenuse}}, \\quad \\cos \\theta = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}}, \\quad \\tan \\theta = \\frac{\\text{Opposite}}{\\text{Adjacent}} \\\\ \\csc \\theta &= \\frac{1}{\\sin \\theta}, \\quad \\sec \\theta = \\frac{1}{\\cos \\theta}, \\quad \\cot \\theta = \\frac{1}{\\tan \\theta} = \\frac{\\cos \\theta}{\\sin \\theta} \\end{aligned}",
                "note_en": "Remember: SOH CAH TOA or Some People Have Curly Brown Hair Turn Permanently Black.",
                "note_te": "లంబకోణ త్రిభుజ భుజాల నిష్పత్తులు."
            },
            {
                "title_en": "Specific Angles Table (0°, 30°, 45°, 60°, 90°)",
                "title_te": "నిర్దిష్ట కోణాల త్రికోణమితి విలువల పట్టిక",
                "latex": "\\begin{array}{|c|c|c|c|c|c|} \\hline \\text{Ratio} & 0^\\circ & 30^\\circ & 45^\\circ & 60^\\circ & 90^\\circ \\\\ \\hline \\sin & 0 & 1/2 & 1/\\sqrt{2} & \\sqrt{3}/2 & 1 \\\\ \\hline \\cos & 1 & \\sqrt{3}/2 & 1/\\sqrt{2} & 1/2 & 0 \\\\ \\hline \\tan & 0 & 1/\\sqrt{3} & 1 & \\sqrt{3} & \\text{Not Defined} \\\\ \\hline \\end{array}",
                "note_en": "Trick to generate: write 0/4, 1/4, 2/4, 3/4, 4/4 and take square root for sin!",
                "note_te": "గుర్తుంచుకునే కిటుకు: 0, 1, 2, 3, 4 లను 4 చే భాగించి వర్గమూలం తీసుకుంటే sin విలువలు వస్తాయి!"
            },
            {
                "title_en": "3 Fundamental Trigonometric Identities",
                "title_te": "3 ప్రాథమిక త్రికోణమితి సర్వసమీకరణాలు",
                "latex": "\\begin{aligned} \\sin^2 \\theta + \\cos^2 \\theta &= 1 \\\\ \\sec^2 \\theta - \\tan^2 \\theta &= 1 \\quad (\\sec \\theta + \\tan \\theta = \\frac{1}{\\sec \\theta - \\tan \\theta}) \\\\ \\csc^2 \\theta - \\cot^2 \\theta &= 1 \\quad (\\csc \\theta + \\cot \\theta = \\frac{1}{\\csc \\theta - \\cot \\theta}) \\end{aligned}",
                "note_en": "GUARANTEED 4-mark identity proof question in board exams!",
                "note_te": "బోర్డు పరీక్షల్లో గ్యారెంటీగా వచ్చే 4 మార్కుల నిరూపణ ప్రశ్న!"
            }
        ],
        "mnemonic": "Sine squares with Cosine by addition (+); Secant squares with Tan by subtraction (-); Cosec squares with Cot by subtraction (-)."
    },
    {
        "id": 12,
        "name_en": "Applications of Trigonometry",
        "name_te": "త్రికోణమితి అనువర్తనాలు",
        "category": "Trigonometry",
        "weightage": "6 Marks",
        "formulas": [
            {
                "title_en": "Angle of Elevation and Depression",
                "title_te": "ఊర్ధ్వ కోణం మరియు నిమ్న కోణం",
                "latex": "\\tan \\theta = \\frac{\\text{Height of Object } (h)}{\\text{Distance from Object } (d)} \\implies h = d \\tan \\theta",
                "note_en": "Angle of Elevation = Looking upwards from horizontal. Angle of Depression = Looking downwards from horizontal. (Both are equal due to alternate interior angles).",
                "note_te": "ఊర్ధ్వ కోణం = క్షితిజ సమాంతర రేఖకు పైకి చూసినపుడు. నిమ్న కోణం = కిందికి చూసినపుడు. (ఏకాంతర కోణాలు కాబట్టి రెండూ సమానం)."
            }
        ],
        "mnemonic": "Draw the diagram first! 90% of marks come from the correct right-triangle sketch and tan theta = height / distance."
    },
    {
        "id": 13,
        "name_en": "Probability",
        "name_te": "సంభావ్యత",
        "category": "Statistics & Probability",
        "weightage": "6 Marks",
        "formulas": [
            {
                "title_en": "Theoretical (Classical) Probability",
                "title_te": "సంభావ్యత ప్రాథమిక సూత్రం",
                "latex": "P(E) = \\frac{\\text{Number of outcomes favorable to } E}{\\text{Total number of possible outcomes}} = \\frac{n(E)}{n(S)}",
                "note_en": "Where 0 <= P(E) <= 1 always. P(Sure event) = 1, P(Impossible event) = 0.",
                "note_te": "ఎల్లప్పుడూ 0 <= P(E) <= 1 ఉంటుంది. ఖచ్చిత ఘటనకు 1, అసాధ్య ఘటనకు 0."
            },
            {
                "title_en": "Complementary Event",
                "title_te": "పూరక ఘటన",
                "latex": "P(E) + P(\\bar{E}) = 1 \\implies P(\\bar{E}) = 1 - P(E)",
                "note_en": "Event E and Not E are complementary.",
                "note_te": "ఘటన E మరియు E-కాకపోవడం పూరక ఘటనలు."
            }
        ],
        "mnemonic": "Probability can NEVER be negative and NEVER be greater than 1! Total pack of cards = 52 (26 Red, 26 Black; 12 Face cards)."
    },
    {
        "id": 14,
        "name_en": "Statistics",
        "name_te": "సాంఖ్యక శాస్త్రం",
        "category": "Statistics & Probability",
        "weightage": "10 - 12 Marks (Highest Yield!)",
        "formulas": [
            {
                "title_en": "Direct Method for Mean",
                "title_te": "ప్రత్యక్ష పద్ధతిలో సగటు",
                "latex": "\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}",
                "note_en": "Where x_i is the class mark = (Lower limit + Upper limit) / 2.",
                "note_te": "ఇక్కడ x_i = తరగతి మధ్య విలువ = (దిగువ హద్దు + ఎగువ హద్దు) / 2."
            },
            {
                "title_en": "Step-Deviation Method for Mean (Board Exam Favorite)",
                "title_te": "పద విచలన పద్ధతిలో సగటు",
                "latex": "\\bar{x} = a + \\left( \\frac{\\sum f_i u_i}{\\sum f_i} \\right) \\times h, \\quad u_i = \\frac{x_i - a}{h}",
                "note_en": "Where a = assumed mean, h = class size (width), u_i = step deviation.",
                "note_te": "ఇక్కడ a = ఊహించిన సగటు, h = తరగతి పొడవు, u_i = (x_i - a) / h."
            },
            {
                "title_en": "Mode for Grouped Data",
                "title_te": "వర్గీకృత దత్తాంశ బాహుళకం",
                "latex": "\\text{Mode} = l + \\left( \\frac{f_1 - f_0}{2f_1 - f_0 - f_2} \\right) \\times h",
                "note_en": "Where l = lower limit of modal class, f1 = modal frequency, f0 = preceding frequency, f2 = succeeding frequency, h = class size.",
                "note_te": "ఇక్కడ l = బాహుళక తరగతి దిగువ హద్దు, f1 = బాహుళక పౌనఃపున్యం, f0 = ముందు తరగతి పౌనఃపున్యం, f2 = తర్వాతి తరగతి పౌనఃపున్యం, h = తరగతి పొడవు."
            },
            {
                "title_en": "Median for Grouped Data",
                "title_te": "వర్గీకృత దత్తాంశ మధ్యగతం",
                "latex": "\\text{Median} = l + \\left( \\frac{\\frac{n}{2} - cf}{f} \\right) \\times h",
                "note_en": "Where l = lower boundary of median class, n = total frequency, cf = cumulative frequency of preceding class, f = frequency of median class, h = class size.",
                "note_te": "ఇక్కడ l = మధ్యగత తరగతి దిగువ హద్దు, n = మొత్తం పౌనఃపున్యం, cf = ముందు తరగతి సంచిత పౌనఃపున్యం, f = మధ్యగత తరగతి పౌనఃపున్యం, h = తరగతి పొడవు."
            }
        ],
        "mnemonic": "Guaranteed 8-mark question in Section IV comes from Statistics! Learn Step-deviation mean, Median, and Mode formulas thoroughly."
    }
]

# =============================================================================
# 2. EXAM PREP: PASS SSC WITH 40+ MARKS GUARANTEE
# =============================================================================
EXAM_PREP_DATA = {
    "title_en": "Pass SSC Math with 40+ Marks Guarantee",
    "title_te": "పాస్ మార్కుల వ్యూహం - 40+ మార్కుల గ్యారెంటీ",
    "slogan_en": "Targeting 35-40 pass marks? Master just 5 easy chapters and 15 guaranteed questions to pass with flying colors!",
    "slogan_te": "గణితంలో పాస్ మార్కులు కావాలా? కేవలం ఈ 5 అధ్యాయాలు మరియు 15 గ్యారెంటీ ప్రశ్నలు నేర్చుకుంటే సునాయాసంగా 40+ మార్కులు సాధించవచ్చు!",
    
    # 5 High-yield chapters breakdown
    "high_yield_chapters": [
        {
            "rank": 1,
            "chapter_id": 14,
            "name_en": "Statistics",
            "name_te": "సాంఖ్యక శాస్త్రం",
            "marks": "10 - 12 Marks",
            "why_easy_en": "Guaranteed 8-mark problem in Section IV. Just memorize Step-Deviation Mean or Mode formula and fill the table. No complicated geometry or equations!",
            "why_easy_te": "సెక్షన్ 4 లో ఖచ్చితంగా 8 మార్కుల లెక్క వస్తుంది. కేవలం పట్టిక వేసి సగటు లేదా బాహుళకం సూత్రం వేస్తే చాలు. పూర్తి మార్కులు పడతాయి!",
            "target_topics": ["Step-deviation Mean", "Median formula", "Mode formula", "Less than Ogive curve"]
        },
        {
            "rank": 2,
            "chapter_id": 1,
            "name_en": "Real Numbers",
            "name_te": "వాస్తవ సంఖ్యలు",
            "marks": "8 Marks",
            "why_easy_en": "Proving sqrt(2), sqrt(3), or sqrt(5) is irrational is guaranteed (4 or 8 marks). Euclid HCF is another guaranteed 2 marks.",
            "why_easy_te": "రూట్ 2, రూట్ 3 లేదా రూట్ 5 కరణీయ సంఖ్య అని నిరూపించే లెక్క (4 లేదా 8 మార్కులు) ప్రతి పేపర్‌లో వస్తుంది. యూక్లిడ్ గ.సా.భా 2 మార్కులు.",
            "target_topics": ["Prove sqrt(p) is irrational", "Euclid's Division Algorithm HCF", "Laws of Logarithms"]
        },
        {
            "rank": 3,
            "chapter_id": 2,
            "name_en": "Sets",
            "name_te": "సమితులు",
            "marks": "6 Marks",
            "why_easy_en": "Easiest chapter in the entire syllabus! Venn diagrams of A U B, A ∩ B, A - B and finding union/intersection give 100% full marks with zero calculation errors.",
            "why_easy_te": "10వ తరగతి సిలబస్ లోనే అత్యంత తేలికైన పాఠం! వెన్ చిత్రాలు మరియు సమితుల సమ్మేళనం, ఛేదనం లెక్కలు సులభంగా పూర్తి మార్కులు తెచ్చిపెడతాయి.",
            "target_topics": ["Venn Diagrams (A U B, A ∩ B, A - B)", "Roster form & Set-builder form", "n(A U B) = n(A) + n(B) - n(A ∩ B)"]
        },
        {
            "rank": 4,
            "chapter_id": 3,
            "name_en": "Polynomials",
            "name_te": "బహుపదులు",
            "marks": "8 Marks",
            "why_easy_en": "Graph of quadratic polynomial (finding zeroes on graph) is frequently in Section IV (8 marks). Finding quadratic polynomial from zeroes gives 2 to 4 marks.",
            "why_easy_te": "వర్గ బహుపది గ్రాఫ్ (శూన్యాలు కనుగొనుట) గ్రాఫ్ ప్రశ్నగా 8 మార్కులకు వస్తుంది. శూన్యాల ద్వారా వర్గ బహుపదిని రాయడం 2-4 మార్కులు.",
            "target_topics": ["Zeroes of Quadratic Polynomial & Verification", "Quadratic Graph p(x) = x^2 - x - 6", "Forming polynomial from sum & product"]
        },
        {
            "rank": 5,
            "chapter_id": 6,
            "name_en": "Progressions",
            "name_te": "శ్రేఢులు",
            "marks": "6 - 8 Marks",
            "why_easy_en": "Only two core formulas: an = a + (n-1)d and Sn = n/2[2a + (n-1)d]. Direct substitution gives 4 to 6 marks.",
            "why_easy_te": "కేవలం రెండు సూత్రాలు మాత్రమే: a_n = a + (n-1)d మరియు S_n = n/2[2a + (n-1)d]. సూత్రంలో విలువలు ప్రతిక్షేపిస్తే సరిపోతుంది.",
            "target_topics": ["Find n-th term of AP", "Sum of first n terms", "Find which term is equal to a given number"]
        }
    ],

    # 15 Guaranteed Must-Pass Questions Bank
    "guaranteed_questions": [
        {
            "id": "q1",
            "chapter": "Real Numbers",
            "chapter_id": 1,
            "marks": "4 or 8 Marks",
            "title_en": "Prove that √5 is an irrational number",
            "title_te": "√5 ఒక కరణీయ సంఖ్య అని నిరూపించండి",
            "query": "Prove that sqrt(5) is an irrational number",
            "exam_tip": "Start with: 'Let us assume on the contrary that sqrt(5) is rational...'. Write every step neatly to get full marks."
        },
        {
            "id": "q2",
            "chapter": "Real Numbers",
            "chapter_id": 1,
            "marks": "2 Marks",
            "title_en": "Find HCF of 900 and 270 using Euclid's division algorithm",
            "title_te": "యూక్లిడ్ భాగహార న్యాయం ఉపయోగించి 900 మరియు 270 ల గ.సా.భా కనుగొనండి",
            "query": "Find the HCF of 900 and 270 by using Euclid division algorithm",
            "exam_tip": "Write formula a = bq + r (0 <= r < b). Step 1: 900 = 270 * 3 + 90. Step 2: 270 = 90 * 3 + 0. Remainder is 0, so HCF is 90."
        },
        {
            "id": "q3",
            "chapter": "Real Numbers",
            "chapter_id": 1,
            "marks": "2 Marks",
            "title_en": "Find HCF of 1.2 and 0.12 using Euclid's algorithm",
            "title_te": "యూక్లిడ్ విశేషవిధి ద్వారా 1.2 మరియు 0.12 ల గ.సా.భా కనుగొని సమాధానాన్ని సమర్థించండి",
            "query": "Can you find the HCF of 1.2 and 0.12 by using Euclid division algorithm? Justify your answer.",
            "exam_tip": "Multiply by 100 to get integers 120 and 12. HCF(120, 12) = 12. Scale back by dividing by 100 = 0.12."
        },
        {
            "id": "q4",
            "chapter": "Sets",
            "chapter_id": 2,
            "marks": "4 Marks",
            "title_en": "If A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7}, find A U B, A ∩ B, A - B and B - A",
            "title_te": "A = {1, 2, 3, 4, 5} మరియు B = {4, 5, 6, 7} అయితే A U B, A ∩ B, A - B మరియు B - A లను కనుగొనండి",
            "query": "If A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7}, find A U B, A ∩ B, A - B, B - A",
            "exam_tip": "Do not repeat elements in sets! A - B = {1, 2, 3} and B - A = {6, 7}."
        },
        {
            "id": "q5",
            "chapter": "Sets",
            "chapter_id": 2,
            "marks": "4 Marks",
            "title_en": "Draw Venn diagrams to illustrate A U B, A ∩ B, and A - B",
            "title_te": "A U B, A ∩ B, మరియు A - B లను చూపే వెన్ చిత్రాలను గీయండి",
            "query": "Draw Venn diagrams for A U B, A ∩ B and A - B",
            "exam_tip": "Use a coin or bottle cap to draw neat circles. Shade the appropriate region clearly."
        },
        {
            "id": "q6",
            "chapter": "Polynomials",
            "chapter_id": 3,
            "marks": "4 Marks",
            "title_en": "Find zeroes of x² - 2x - 8 and verify relationship with coefficients",
            "title_te": "x² - 2x - 8 బహుపదికి శూన్యాలు కనుగొని, గుణకాలతో సంబంధాన్ని సరిచూడండి",
            "query": "Find the zeroes of the quadratic polynomial x^2 - 2x - 8 and verify the relationship between the zeroes and the coefficients",
            "exam_tip": "Roots are 4 and -2. Sum = 4 + (-2) = 2 = -(-2)/1. Product = 4 * (-2) = -8 = -8/1."
        },
        {
            "id": "q7",
            "chapter": "Polynomials",
            "chapter_id": 3,
            "marks": "2 Marks",
            "title_en": "Find quadratic polynomial whose zeroes are 2 and -1/3",
            "title_te": "శూన్యాలు 2 మరియు -1/3 గా గల వర్గ బహుపదిని కనుగొనండి",
            "query": "Find the quadratic polynomial whose zeroes are 2 and -1/3",
            "exam_tip": "Sum = 5/3, Product = -2/3. p(x) = k[x^2 - (5/3)x - 2/3]. Taking k = 3 gives 3x^2 - 5x - 2."
        },
        {
            "id": "q8",
            "chapter": "Quadratic Equations",
            "chapter_id": 5,
            "marks": "4 Marks",
            "title_en": "Find the roots of quadratic equation: x² + 5x + 6 = 0",
            "title_te": "వర్గ సమీకరణం x² + 5x + 6 = 0 యొక్క మూలాలను కనుగొనండి",
            "query": "Find roots of x^2 + 5x + 6 = 0",
            "exam_tip": "Split middle term: (x + 2)(x + 3) = 0 => x = -2, -3. Always box the final answer."
        },
        {
            "id": "q9",
            "chapter": "Progressions",
            "chapter_id": 6,
            "marks": "2 or 4 Marks",
            "title_en": "Find the 10th term of the AP: 2, 7, 12, ...",
            "title_te": "అంకశ్రేఢి 2, 7, 12, ... లో 10వ పదాన్ని కనుగొనండి",
            "query": "Find the 10th term of the AP 2, 7, 12, ...",
            "exam_tip": "a = 2, d = 7 - 2 = 5, n = 10. an = 2 + (10-1)*5 = 2 + 45 = 47."
        },
        {
            "id": "q10",
            "chapter": "Progressions",
            "chapter_id": 6,
            "marks": "4 Marks",
            "title_en": "Find the sum of first 20 terms of AP: 1, 4, 7, 10, ...",
            "title_te": "అంకశ్రేఢి 1, 4, 7, 10, ... మొదటి 20 పదాల మొత్తం కనుగొనండి",
            "query": "Find the sum of first 20 terms of the AP: 1, 4, 7, 10, ...",
            "exam_tip": "a = 1, d = 3, n = 20. S20 = 20/2 * [2(1) + 19(3)] = 10 * [2 + 57] = 590."
        },
        {
            "id": "q11",
            "chapter": "Coordinate Geometry",
            "chapter_id": 7,
            "marks": "2 Marks",
            "title_en": "Find distance between points (2, 3) and (4, 1)",
            "title_te": "(2, 3) మరియు (4, 1) బిందువుల మధ్య దూరాన్ని కనుగొనండి",
            "query": "Find the distance between the points (2, 3) and (4, 1)",
            "exam_tip": "d = sqrt((4-2)^2 + (1-3)^2) = sqrt(4 + 4) = sqrt(8) = 2*sqrt(2) units."
        },
        {
            "id": "q12",
            "chapter": "Coordinate Geometry",
            "chapter_id": 7,
            "marks": "4 Marks",
            "title_en": "Find the coordinates of the midpoint of segment joining (1, -2) and (-3, 4)",
            "title_te": "(1, -2) మరియు (-3, 4) బిందువులను కలిపే రేఖాఖండం మధ్య బిందువు నిరూపకాలు కనుగొనండి",
            "query": "Find the midpoint of the line segment joining (1, -2) and (-3, 4)",
            "exam_tip": "M = ((1 + (-3))/2, (-2 + 4)/2) = (-2/2, 2/2) = (-1, 1)."
        },
        {
            "id": "q13",
            "chapter": "Trigonometry",
            "chapter_id": 11,
            "marks": "4 Marks",
            "title_en": "Evaluate: 2 tan² 45° + cos² 30° - sin² 60°",
            "title_te": "విలువను కనుగొనండి: 2 tan² 45° + cos² 30° - sin² 60°",
            "query": "Evaluate 2 tan^2 45 + cos^2 30 - sin^2 60",
            "exam_tip": "tan 45° = 1, cos 30° = sqrt(3)/2, sin 60° = sqrt(3)/2. Result = 2(1)^2 + 3/4 - 3/4 = 2."
        },
        {
            "id": "q14",
            "chapter": "Statistics",
            "chapter_id": 14,
            "marks": "8 Marks",
            "title_en": "Find the Mean of grouped frequency distribution using Step-Deviation method",
            "title_te": "పద విచలన పద్ధతిలో ఇచ్చిన పౌనఃపున్య విభాజనానికి సగటును కనుగొనండి",
            "query": "Find the mean of the data using step-deviation method",
            "exam_tip": "Make 5 columns: Class Interval, Frequency fi, Class Mark xi, ui = (xi - a)/h, fi*ui. Apply x_bar = a + (sum fi*ui / sum fi) * h."
        },
        {
            "id": "q15",
            "chapter": "Statistics",
            "chapter_id": 14,
            "marks": "8 Marks",
            "title_en": "Find the Mode of grouped distribution",
            "title_te": "ఇచ్చిన పౌనఃపున్య విభాజనానికి బాహుళకాన్ని (Mode) కనుగొనండి",
            "query": "Find the mode of the grouped frequency distribution",
            "exam_tip": "Identify highest frequency f1. The class is modal class. Apply Mode = l + [(f1 - f0)/(2f1 - f0 - f2)] * h."
        }
    ],

    # 5-Day Study Plan for Guaranteed 40+ Marks
    "five_day_plan": [
        {
            "day": 1,
            "title_en": "Day 1: Statistics Mastery (10 - 12 Marks)",
            "title_te": "మొదటి రోజు: సాంఖ్యక శాస్త్రం (10-12 మార్కులు)",
            "hours": "2.5 Hours",
            "tasks_en": [
                "Learn Step-Deviation Mean formula and practice 2 textbook problems (Ex 14.1).",
                "Learn Mode formula and practice 2 problems (Ex 14.2).",
                "Practice drawing 1 Less than Ogive curve."
            ],
            "tasks_te": [
                "పద విచలన పద్ధతి సగటు సూత్రం నేర్చుకుని, 2 లెక్కలు సాధించండి.",
                "బాహుళకం సూత్రం నేర్చుకుని, 2 లెక్కలు సాధించండి.",
                "ఒక ఆరోహణ సంచిత పౌనఃపున్య వక్రం (ఓజీవ్) గీయడం ప్రాక్టీస్ చేయండి."
            ],
            "marks_secured": "12 Marks"
        },
        {
            "day": 2,
            "title_en": "Day 2: Real Numbers (8 Marks)",
            "title_te": "రెండో రోజు: వాస్తవ సంఖ్యలు (8 మార్కులు)",
            "hours": "2 Hours",
            "tasks_en": [
                "Practice proof of irrationality for √2, √3, √5 (Guaranteed 4 or 8 marks!).",
                "Practice Euclid's division algorithm HCF for 3 problem sets (Ex 1.1).",
                "Memorize all 5 laws of logarithms."
            ],
            "tasks_te": [
                "√2, √3, √5 లు కరణీయ సంఖ్యలని నిరూపించే లెక్క ప్రాక్టీస్ చేయండి.",
                "యూక్లిడ్ భాగహార న్యాయం ద్వారా గ.సా.భా కనుగొనే 3 లెక్కలు సాధించండి.",
                "సంవర్గమానాల 5 ప్రాథమిక సూత్రాలు కంఠస్థం చేయండి."
            ],
            "marks_secured": "+8 Marks (Total 20)"
        },
        {
            "day": 3,
            "title_en": "Day 3: Sets (6 Marks)",
            "title_te": "మూడో రోజు: సమితులు (6 మార్కులు)",
            "hours": "1.5 Hours",
            "tasks_en": [
                "Practice finding A U B, A ∩ B, A - B, and B - A.",
                "Draw Venn diagrams for A U B, A ∩ B, A - B.",
                "Learn Roster and Set-builder form conversion."
            ],
            "tasks_te": [
                "A U B, A ∩ B, A - B, B - A కనుగొనే లెక్కలు సాధించండి.",
                "వీటికి సంబంధించిన వెన్ చిత్రాలు గీయడం ప్రాక్టీస్ చేయండి.",
                "రోస్టర్ రూపం మరియు సమితి నిర్మాణ రూపం మార్పులను నేర్చుకోండి."
            ],
            "marks_secured": "+6 Marks (Total 26)"
        },
        {
            "day": 4,
            "title_en": "Day 4: Polynomials (8 Marks)",
            "title_te": "నాల్గో రోజు: బహుపదులు (8 మార్కులు)",
            "hours": "2 Hours",
            "tasks_en": [
                "Practice finding zeroes of quadratic polynomial x^2 - 2x - 8 and verify.",
                "Practice drawing graph of p(x) = x^2 - x - 6 to find zeroes.",
                "Form quadratic polynomial from given zeroes: p(x) = k[x^2 - (a+b)x + ab]."
            ],
            "tasks_te": [
                "వర్గ బహుపది శూన్యాలు కనుగొని సరిచూసే లెక్కలు చేయండి.",
                "వర్గ బహుపది గ్రాఫ్ గీసి శూన్యాలు కనుగొనే పద్ధతి ప్రాక్టీస్ చేయండి.",
                "శూన్యాల ద్వారా వర్గ బహుపదిని కనుగొనే సూత్రం ప్రాక్టీస్ చేయండి."
            ],
            "marks_secured": "+8 Marks (Total 34)"
        },
        {
            "day": 5,
            "title_en": "Day 5: Progressions & Coordinate Geometry (10 Marks)",
            "title_te": "ఐదో రోజు: శ్రేఢులు & నిరూపక జ్యామితి (10 మార్కులు)",
            "hours": "2.5 Hours",
            "tasks_en": [
                "Practice AP n-th term an = a + (n-1)d and sum Sn = n/2[2a + (n-1)d].",
                "Practice Distance formula d = sqrt((x2-x1)^2 + (y2-y1)^2).",
                "Practice Midpoint formula ((x1+x2)/2, (y1+y2)/2).",
                "Quick formula revision for all chapters."
            ],
            "tasks_te": [
                "అంకశ్రేఢి nవ పదం మరియు n పదాల మొత్తం లెక్కలు సాధించండి.",
                "దూరం సూత్రం మరియు మధ్య బిందువు సూత్రం లెక్కలు ప్రాక్టీస్ చేయండి.",
                "అన్ని చాప్టర్ల సూత్రాలను ఒకసారి మననం చేసుకోండి."
            ],
            "marks_secured": "+10 Marks (Total 44+ Marks! Passed with distinction!)"
        }
    ]
}

# =============================================================================
# 3. PREVIOUS SSC BOARD EXAM PAPERS (AP & TS)
# =============================================================================
PAST_PAPERS_DATA = [
    {
        "year": "2024",
        "state": "Telangana (TS)",
        "exam_type": "Annual Public Examination (Single Paper - 80 Marks)",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Latest single-paper format examination consisting of Section I, II, III, and IV with internal choice in Section IV.",
        "download_links": [
            {
                "label": "TS SSC 2024 Math Paper (Official BSE TS)",
                "url": "https://bse.telangana.gov.in/",
                "type": "Official Board Portal"
            },
            {
                "label": "TS SSC 2024 Math Question Paper & Key (Sakshi Education)",
                "url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
                "type": "Paper & Answer Key"
            }
        ]
    },
    {
        "year": "2024",
        "state": "Andhra Pradesh (AP)",
        "exam_type": "Annual Public Examination (100 Marks)",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "AP SSC 2024 Board question paper with 33 questions across 4 sections.",
        "download_links": [
            {
                "label": "AP SSC 2024 Math Paper (BSE AP Official)",
                "url": "https://bse.ap.gov.in/",
                "type": "Official Board Portal"
            },
            {
                "label": "AP SSC 2024 Math Paper & Solutions (Eenadu Pratibha)",
                "url": "https://www.eenadupratibha.net/ap-tenth/",
                "type": "Paper & Solutions"
            }
        ]
    },
    {
        "year": "2023",
        "state": "Telangana (TS)",
        "exam_type": "Annual Public Examination",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "TS SSC 2023 Board Examination Mathematics Question Paper with model answer key.",
        "download_links": [
            {
                "label": "TS SSC 2023 Math Paper & Solutions",
                "url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
                "type": "Question Paper PDF"
            }
        ]
    },
    {
        "year": "2023",
        "state": "Andhra Pradesh (AP)",
        "exam_type": "Annual Public Examination",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "AP SSC 2023 Board Mathematics Question Paper.",
        "download_links": [
            {
                "label": "AP SSC 2023 Math Question Paper",
                "url": "https://www.eenadupratibha.net/ap-tenth/",
                "type": "Question Paper PDF"
            }
        ]
    },
    {
        "year": "2022",
        "state": "Telangana & AP",
        "exam_type": "Board Examination Papers",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Post-pandemic streamlined question papers with increased internal choice.",
        "download_links": [
            {
                "label": "TS & AP 2022 Math Board Papers",
                "url": "https://www.sakshieducation.com/",
                "type": "Archive"
            }
        ]
    },
    {
        "year": "Model Paper 2025",
        "state": "AP & TS State Boards",
        "exam_type": "Official Model Question Paper & Blueprint",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Official SCERT blueprint demonstrating mark weightage by academic standards (Problem Solving: 40%, Reasoning & Proof: 20%, Communication: 10%, Connection: 15%, Representation & Visualization: 15%).",
        "download_links": [
            {
                "label": "SCERT SSC Math Blueprint & Weightage Table",
                "url": "https://scert.telangana.gov.in/",
                "type": "Official Blueprint"
            }
        ]
    }
]

# =============================================================================
# 4. TEXTBOOK QUESTION RETRIEVER
# =============================================================================
def get_textbook_question(exercise_id: str, question_num: int = 1) -> dict:
    """
    Extracts the exact question text and sub-questions for a given exercise and question number
    from the textbook index snippet.
    """
    if not os.path.exists(INDEX_PATH):
        return {
            "exercise": exercise_id,
            "question_number": question_num,
            "question_text": f"Exercise {exercise_id}, Question {question_num}",
            "sub_questions": []
        }
        
    try:
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            index_data = json.load(f)
    except Exception:
        return {
            "exercise": exercise_id,
            "question_number": question_num,
            "question_text": f"Exercise {exercise_id}, Question {question_num}",
            "sub_questions": []
        }
        
    ex_data = index_data.get("exercises", {}).get(exercise_id, {})
    snippet = ex_data.get("snippet", "")
    
    # Try parsing questions starting with numbers like 1. , 2. , 3.
    qs = re.findall(r'(?:^|\n)(\d+)\.\s+(.*?)(?=\n\d+\.|\n\d+\.\d+|\Z)', snippet, re.DOTALL)
    
    found_q = None
    for q_idx, q_body in qs:
        if str(q_idx) == str(question_num):
            found_q = q_body.strip()
            break
            
    # Default fallback if specific number wasn't found in snippet
    if not found_q:
        if qs and int(question_num) <= len(qs):
            found_q = qs[int(question_num) - 1][1].strip()
        else:
            # Provide standard textbook question based on exercise
            found_q = get_curated_exercise_question(exercise_id, question_num)
            
    # Clean up snippet artifacts
    found_q = re.sub(r'\s+', ' ', found_q).strip()
    
    # Extract sub-questions like (i) ..., (ii) ...
    sub_parts = []
    sub_matches = re.findall(r'(\([ivxIVX0-9]+\))\s*([^\(]+)', found_q)
    for part, p_text in sub_matches:
        sub_parts.append({
            "part": part.strip(),
            "text": p_text.strip()
        })
        
    return {
        "exercise": exercise_id,
        "question_number": int(question_num),
        "question_text": found_q,
        "sub_questions": sub_parts,
        "total_questions_in_exercise": max(len(qs), 8)
    }

def get_curated_exercise_question(exercise_id: str, q_num: int) -> str:
    """Curated standard questions for major SSC exercises if snippet is cut short."""
    curated = {
        "1.1": {
            1: "Use Euclid's algorithm to find the HCF of: (i) 900 and 270 (ii) 196 and 38220 (iii) 1651 and 2032",
            2: "Use division algorithm to show that any positive odd integer is of the form 6q + 1, or 6q + 3 or 6q + 5, where q is some integer.",
            3: "Use division algorithm to show that the square of any positive integer is of the form 3p or 3p + 1.",
            4: "Use division algorithm to show that the cube of any positive integer is of the form 9m, 9m + 1 or 9m + 8."
        },
        "1.2": {
            1: "Express each number as a product of its prime factors: (i) 140 (ii) 156 (iii) 3825 (iv) 5005 (v) 7429",
            2: "Find the LCM and HCF of the integers by prime factorisation method: (i) 12, 15 and 21 (ii) 17, 23 and 29",
            3: "Check whether 6^n can end with the digit 0 for any natural number n."
        },
        "1.3": {
            1: "Prove that √5 is irrational.",
            2: "Prove that 3 + 2√5 is irrational.",
            3: "Prove that the following are irrationals: (i) 1/√2 (ii) 7√5 (iii) 6 + √2"
        },
        "1.4": {
            1: "Without actually performing the long division, state whether the following rational numbers will have a terminating decimal expansion or a non-terminating repeating decimal expansion: (i) 13/3125 (ii) 11/12 (iii) 64/455 (iv) 15/1600"
        },
        "1.5": {
            1: "Determine the value of the following: (i) log2 512 (ii) log5 1/625 (iii) log3 243 (iv) log10 0.001",
            2: "Write the following expressions as a single logarithm: 2 log 3 + 3 log 5 - 5 log 2"
        },
        "2.1": {
            1: "Which of the following are sets? Justify your answer.",
            2: "If A = {0, 2, 4, 6}, B = {3, 5, 7} and C = {p, q, r}, then fill the appropriate symbol ∈ or ∉ in the blanks.",
            3: "Express the following in state builder form: (i) {3, 6, 9, 12} (ii) {2, 4, 8, 16, 32} (iii) {5, 25, 125, 625}"
        },
        "2.2": {
            1: "If A = {1, 2, 3, 4} and B = {1, 2, 3, 5, 6}, then find A ∩ B and B ∩ A. Are they equal?",
            2: "A = {0, 2, 4}, find A ∩ ∅ and A ∩ A. Comment.",
            3: "If A = {2, 4, 6, 8, 10} and B = {3, 6, 9, 12, 15}, find A - B and B - A."
        },
        "3.1": {
            1: "If p(x) = 5x^7 - 6x^5 + 7x - 6, find (i) degree of p(x) (ii) coefficient of x^5 (iii) constant term.",
            2: "State which of the following statements are true and which are false."
        },
        "3.2": {
            1: "The graphs of y = p(x) are given in figures below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.",
            2: "Find the zeroes of the given polynomials: (i) p(x) = 3x (ii) p(x) = x^2 + 5x + 6"
        },
        "3.3": {
            1: "Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients: (i) x^2 - 2x - 8 (ii) 4s^2 - 4s + 1 (iii) 6x^2 - 3 - 7x",
            2: "Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively: (i) 1/4, -1 (ii) √2, 1/3 (iii) 0, √5 (iv) 1, 1"
        },
        "5.1": {
            1: "Check whether the following are quadratic equations: (i) (x + 1)^2 = 2(x - 3) (ii) x^2 - 2x = (-2)(3 - x)"
        },
        "5.2": {
            1: "Find the roots of the following quadratic equations by factorisation: (i) x^2 - 3x - 10 = 0 (ii) 2x^2 + x - 6 = 0 (iii) √2 x^2 + 7x + 5√2 = 0",
            2: "Find two numbers whose sum is 27 and product is 182."
        },
        "6.1": {
            1: "In which of the following situations, does the list of numbers involved make an arithmetic progression, and why?",
            2: "Write first four terms of the AP, when the first term a and the common difference d are given as follows: (i) a = 10, d = 10 (ii) a = -2, d = 0"
        },
        "6.2": {
            1: "Fill in the blanks in the following table, given that a is the first term, d the common difference and an the nth term of the AP.",
            2: "Choose the correct choice in the following and justify: (i) 30th term of the AP: 10, 7, 4, ... is"
        },
        "7.1": {
            1: "Find the distance between the following pairs of points: (i) (2, 3), (4, 1) (ii) (-5, 7), (-1, 3) (iii) (a, b), (-a, -b)",
            2: "Find the distance between the points (0, 0) and (36, 15).",
            3: "Determine if the points (1, 5), (2, 3) and (-2, -11) are collinear."
        },
        "11.1": {
            1: "In right angle triangle ABC, 8 cm, 15 cm and 17 cm are the lengths of AB, BC and CA respectively. Then find sin A, cos A and tan A.",
            2: "The sides of a right angled triangle PQR are PQ = 7 cm, QR = 25 cm and ∠P = 90°. Find tan Q - tan R."
        },
        "14.1": {
            1: "A survey was conducted by a group of students as a part of their environment awareness programme. Find the mean number of plants per house.",
            2: "Consider the following distribution of daily wages of 50 workers of a factory. Find the mean daily wages of the workers of the factory by using an appropriate method."
        }
    }
    
    ex_qs = curated.get(exercise_id, {})
    return ex_qs.get(int(q_num), f"Exercise {exercise_id}, Question {q_num}: Solve the textbook problem step-by-step.")
