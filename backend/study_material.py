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
    "five_day_plan": [{'day': 1, 'title_en': 'Day 1: Foundations & Guaranteed Scoring (24+ Marks)', 'title_te': 'మొదటి రోజు: ప్రాథమిక గణితం & గ్యారెంటీ స్కోరింగ్ (24+ మార్కులు)', 'theme_en': 'Real Numbers, Sets & Statistics', 'theme_te': 'వాస్తవ సంఖ్యలు, సమితులు & సాంఖ్యకశాస్త్రం', 'target_marks': '24 - 28 Marks', 'chapters': [{'id': 1, 'name_en': 'Real Numbers', 'name_te': 'వాస్తవ సంఖ్యలు', 'weightage': '6 - 8 Marks', 'questions': [{'id': 'D1-C1-Q1', 'marks': '1 Mark', 'q_en': 'State the Fundamental Theorem of Arithmetic.', 'q_te': 'అంకగణిత ప్రాథమిక సిద్ధాంతాన్ని నిర్వచించండి.', 'trend': 'AP 2023, TS 2024 (Section I)', 'concept': 'Fundamental Theorem of Arithmetic'}, {'id': 'D1-C1-Q2', 'marks': '1 Mark', 'q_en': 'Evaluate log_2 512 and log_10 0.01.', 'q_te': 'log_2 512 మరియు log_10 0.01 విలువలను లెక్కించండి.', 'trend': 'TS 2022, 2024', 'concept': 'Laws of Logarithms'}, {'id': 'D1-C1-Q3', 'marks': '2 Marks', 'q_en': "Use Euclid's division algorithm to find the HCF of 900 and 270.", 'q_te': 'యూక్లిడ్ భాగహార న్యాయం ఉపయోగించి 900 మరియు 270 ల గ.సా.భా కనుగొనండి.', 'trend': 'TS 2023, 2024 (Ex 1.1)', 'concept': "Euclid's Division Lemma: a = bq + r"}, {'id': 'D1-C1-Q4', 'marks': '2 Marks', 'q_en': 'Find the HCF and LCM of 12, 15 and 21 by prime factorisation method.', 'q_te': 'ప్రధాన కారణాంకాల పద్ధతి ద్వారా 12, 15 మరియు 21 ల గ.సా.భా మరియు క.సా.గు కనుగొనండి.', 'trend': 'AP 2022, TS 2023', 'concept': 'Prime Factorisation Tree'}, {'id': 'D1-C1-Q5', 'marks': '2 Marks', 'q_en': 'Without long division, state whether 13/3125 has a terminating or non-terminating decimal expansion.', 'q_te': 'భాగహార ప్రక్రియ చేయకుండానే 13/3125 అంతమయ్యే దశాంశమో లేదా అంతంకాని ఆవర్తన దశాంశమో తెలపండి.', 'trend': 'AP 2024, TS 2023', 'concept': 'q = 2^n * 5^m condition'}, {'id': 'D1-C1-Q6', 'marks': '4 Marks', 'q_en': 'Prove that √5 is irrational.', 'q_te': '√5 ఒక కరణీయ సంఖ్య అని నిరూపించండి.', 'trend': 'TS & AP Most Repeated (Ex 1.3)', 'concept': 'Proof by Contradiction'}, {'id': 'D1-C1-Q7', 'marks': '4 Marks', 'q_en': 'Prove that 3 + 2√5 is an irrational number.', 'q_te': '3 + 2√5 ఒక కరణీయ సంఖ్య అని నిరూపించండి.', 'trend': 'TS 2023, AP 2023 (Section III)', 'concept': 'Irrationality proof'}, {'id': 'D1-C1-Q8', 'marks': '4 Marks', 'q_en': 'If x^2 + y^2 = 25xy, then prove that 2 log(x + y) = 3 log 3 + log x + log y.', 'q_te': 'x^2 + y^2 = 25xy అయితే, 2 log(x + y) = 3 log 3 + log x + log y అని చూపండి.', 'trend': 'TS 2022, 2024 (Ex 1.5)', 'concept': 'Logarithmic Identity'}, {'id': 'D1-C1-Q9', 'marks': '8 Marks', 'q_en': "Show that the square of any positive integer is of the form 3p or 3p + 1 for some integer p using Euclid's division lemma.", 'q_te': 'ఏదేని ధన పూర్ణసంఖ్య వర్గం 3p లేదా 3p + 1 రూపంలో ఉంటుందని యూక్లిడ్ భాగహార న్యాయం ద్వారా చూపండి.', 'trend': 'AP 2024, TS 2023 (Section IV)', 'concept': "Euclid's Lemma on Number Forms"}, {'id': 'D1-C1-Q10', 'marks': '8 Marks', 'q_en': 'Prove that √2 + √3 is irrational.', 'q_te': '√2 + √3 ఒక కరణీయ సంఖ్య అని నిరూపించండి.', 'trend': 'TS 2024 Model Paper, AP 2023', 'concept': 'Double Root Irrationality'}]}, {'id': 2, 'name_en': 'Sets', 'name_te': 'సమితులు', 'weightage': '6 Marks', 'questions': [{'id': 'D1-C2-Q1', 'marks': '1 Mark', 'q_en': 'Write the set A = {x : x is a natural number less than 6} in roster form.', 'q_te': 'A = {x : x అనేది 6 కంటే తక్కువైన సహజ సంఖ్య} ను రోస్టర్ రూపంలో రాయండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Roster and Set-Builder Forms'}, {'id': 'D1-C2-Q2', 'marks': '1 Mark', 'q_en': 'If A = {1, 2, 3, 4} and B = {2, 4, 6}, find n(A ∪ B) and n(A ∩ B).', 'q_te': 'A = {1, 2, 3, 4}, B = {2, 4, 6} అయితే n(A ∪ B) మరియు n(A ∩ B) కనుగొనండి.', 'trend': 'TS 2024', 'concept': 'Cardinality of Sets'}, {'id': 'D1-C2-Q3', 'marks': '2 Marks', 'q_en': 'If A = {2, 4, 6, 8, 10} and B = {3, 6, 9, 12, 15}, find A - B and B - A. Are they equal?', 'q_te': 'A = {2, 4, 6, 8, 10}, B = {3, 6, 9, 12, 15} అయితే A - B మరియు B - A కనుగొనండి. అవి సమానమా?', 'trend': 'TS 2022, 2024 (Ex 2.2)', 'concept': 'Difference of Sets'}, {'id': 'D1-C2-Q4', 'marks': '2 Marks', 'q_en': 'State whether A = {x : x is an even prime} and B = {2} are equal sets. Justify.', 'q_te': 'A = {x : x ఒక సరి ప్రధాన సంఖ్య} మరియు B = {2} లు సమాన సమితులా? సమర్థించండి.', 'trend': 'AP 2023', 'concept': 'Equal and Equivalent Sets'}, {'id': 'D1-C2-Q5', 'marks': '2 Marks', 'q_en': 'Illustrate A ∪ B and A ∩ B using Venn diagrams for disjoint sets.', 'q_te': 'వియుక్త సమితులకు A ∪ B మరియు A ∩ B లను వెన్ చిత్రాల ద్వారా చూపండి.', 'trend': 'TS 2023', 'concept': 'Disjoint Sets & Venn Diagrams'}, {'id': 'D1-C2-Q6', 'marks': '4 Marks', 'q_en': 'If A = {x : x is a prime number < 10} and B = {x : x is an odd number < 10}, verify that n(A ∪ B) = n(A) + n(B) - n(A ∩ B).', 'q_te': 'A = {x : x < 10 ప్రధాన సంఖ్య}, B = {x : x < 10 బేసి సంఖ్య} అయితే n(A ∪ B) = n(A) + n(B) - n(A ∩ B) ను సరిచూడండి.', 'trend': 'TS 2024, AP 2023', 'concept': 'Cardinality Formula Verification'}, {'id': 'D1-C2-Q7', 'marks': '4 Marks', 'q_en': 'Draw Venn diagrams to represent: (i) A ∪ B (ii) A ∩ B (iii) A - B (iv) B - A.', 'q_te': 'వెన్ చిత్రాల ద్వారా క్రింది వాటిని సూచించండి: (i) A ∪ B (ii) A ∩ B (iii) A - B (iv) B - A.', 'trend': 'AP & TS Board Regular', 'concept': 'Standard Venn Diagram Shading'}, {'id': 'D1-C2-Q8', 'marks': '4 Marks', 'q_en': 'If A = {3, 6, 9, 12, 15, 18, 21}, B = {4, 8, 12, 16, 20}, C = {2, 4, 6, 8, 10, 12, 14, 16}, find (i) A - B (ii) A - C (iii) B - C.', 'q_te': 'A, B, C సమితులు ఇచ్చినప్పుడు (i) A - B (ii) A - C (iii) B - C విలువలను కనుగొనండి.', 'trend': 'TS 2023 (Ex 2.2)', 'concept': 'Multiple Set Differences'}, {'id': 'D1-C2-Q9', 'marks': '8 Marks', 'q_en': 'If A = {x : x is a natural number}, B = {x : x is an even natural number}, C = {x : x is an odd natural number}, D = {x : x is a prime number}, find A ∩ B, A ∩ C, A ∩ D, B ∩ C, B ∩ D and C ∩ D.', 'q_te': 'A, B, C, D సమితులు సహజ, సరి, బేసి, ప్రధాన సంఖ్యలైనప్పుడు A ∩ B, A ∩ C, B ∩ C, B ∩ D, C ∩ D లను కనుగొనండి.', 'trend': 'TS 2024 (Ex 2.2 Q4 - Section IV 8M)', 'concept': 'Comprehensive Intersection on Number Types'}, {'id': 'D1-C2-Q10', 'marks': '8 Marks', 'q_en': 'In a school of 100 students, 60 play cricket, 50 play football, and 30 play both. Find using set theory and Venn diagram: (i) How many play either cricket or football? (ii) How many play neither?', 'q_te': '100 మంది విద్యార్థులలో 60 మంది క్రికెట్, 50 మంది ఫుట్\u200cబాల్, 30 మంది రెండూ ఆడితే: (i) కనీసం ఒక ఆట ఆడేవారు (ii) ఏ ఆటా ఆడని వారి సంఖ్య కనుగొనండి.', 'trend': 'AP 2024 Board Model', 'concept': 'Real-world Set Word Problems'}]}, {'id': 14, 'name_en': 'Statistics', 'name_te': 'సాంఖ్యకశాస్త్రం', 'weightage': '10 - 12 Marks', 'questions': [{'id': 'D1-C14-Q1', 'marks': '1 Mark', 'q_en': 'Write the formula for the mean of grouped data using Step-Deviation method and explain each term.', 'q_te': 'పద విచలన పద్ధతిలో వర్గీకృత దత్తాంశ సగటు సూత్రం రాసి, పదాలను వివరించండి.', 'trend': 'TS 2023, 2024 (Section I)', 'concept': 'Mean Formula: a + [Σfi*ui / Σfi] * h'}, {'id': 'D1-C14-Q2', 'marks': '1 Mark', 'q_en': 'Write the formula to find the mode of grouped data and specify each term.', 'q_te': 'వర్గీకృత దత్తాంశ బాహుళకం సూత్రం రాసి, అందులోని ప్రతి పదాన్ని పేర్కొనండి.', 'trend': 'AP 2023, TS 2022', 'concept': 'Mode Formula: l + [(f1 - f0)/(2f1 - f0 - f2)] * h'}, {'id': 'D1-C14-Q3', 'marks': '2 Marks', 'q_en': 'If the mean of observations 6, 8, 9, x, 13 is 10, find the value of x.', 'q_te': '6, 8, 9, x, 13 రాశుల సగటు 10 అయితే x విలువను కనుగొనండి.', 'trend': 'AP 2024 (Section II)', 'concept': 'Direct Arithmetic Mean'}, {'id': 'D1-C14-Q4', 'marks': '2 Marks', 'q_en': "Write the formula for median of grouped data: Median = l + [(n/2 - cf)/f] * h and define 'cf'.", 'q_te': "మధ్యగతం సూత్రం రాసి, అందులోని 'cf' (సంచిత పౌనఃపున్యం) ను వివరించండి.", 'trend': 'TS 2023', 'concept': 'Median Formula & Terms'}, {'id': 'D1-C14-Q5', 'marks': '2 Marks', 'q_en': 'For a distribution, Mode = 45, Mean = 30. Find its Median using empirical relationship: Mode = 3 Median - 2 Mean.', 'q_te': 'బాహుళకం = 45, సగటు = 30 అయితే మధ్యగతాన్ని సూత్రం ద్వారా కనుగొనండి.', 'trend': 'TS 2024', 'concept': 'Empirical Relationship'}, {'id': 'D1-C14-Q6', 'marks': '4 Marks', 'q_en': 'Find the mode of the following data: Marks: 0-10, 10-20, 20-30, 30-40, 40-50; Number of students: 5, 8, 12, 6, 4.', 'q_te': 'తరగతి అంతరాలు: 0-10, 10-20, 20-30, 30-40, 40-50; పౌనఃపున్యాలు: 5, 8, 12, 6, 4 లకు బాహుళకం కనుగొనండి.', 'trend': 'TS 2024 (Ex 14.2)', 'concept': 'Modal Class & Mode Computation'}, {'id': 'D1-C14-Q7', 'marks': '4 Marks', 'q_en': 'Find the median of the following frequency distribution: Class: 20-30, 30-40, 40-50, 50-60, 60-70; Frequency: 4, 12, 20, 9, 5.', 'q_te': 'తరగతి అంతరాలు: 20-30, 30-40, 40-50, 50-60, 60-70 లకు మధ్యగతం కనుగొనండి.', 'trend': 'AP 2023 (Ex 14.3)', 'concept': 'Cumulative Frequency & Median'}, {'id': 'D1-C14-Q8', 'marks': '4 Marks', 'q_en': 'Find the mean daily wages of 50 workers of a factory using Assumed Mean method: Wages: 100-120, 120-140, 140-160, 160-180, 180-200; Workers: 12, 14, 8, 6, 10.', 'q_te': 'ఊహించిన సగటు పద్ధతిలో 50 మంది కార్మికుల సగటు వేతనం కనుగొనండి.', 'trend': 'TS 2023 (Ex 14.1 Q2)', 'concept': 'Assumed Mean Method (a + Σfi*di / Σfi)'}, {'id': 'D1-C14-Q9', 'marks': '8 Marks', 'q_en': 'Calculate the mean marks of students using Step-Deviation Method: Class: 10-25, 25-40, 40-55, 55-70, 70-85, 85-100; Frequency: 2, 3, 7, 6, 6, 6.', 'q_te': 'పద విచలన పద్ధతి ద్వారా విద్యార్థుల సగటు మార్కులను లెక్కించండి.', 'trend': 'TS & AP Most Guaranteed 8M (Ex 14.1)', 'concept': 'Step-Deviation Full Table & Working'}, {'id': 'D1-C14-Q10', 'marks': '8 Marks', 'q_en': "Draw a 'Less than Ogive' curve for the following distribution and find the median from the graph: Daily income: 100-120, 120-140, 140-160, 160-180, 180-200; Workers: 12, 14, 8, 6, 10.", 'q_te': "క్రింది దత్తాంశానికి 'ఆరోహణ సంచిత పౌనఃపున్య వక్రం (Less than Ogive)' గీసి, గ్రాఫ్ ద్వారా మధ్యగతం కనుగొనండి.", 'trend': 'TS 2024, AP 2024 (Ex 14.4 Graph Question)', 'concept': 'Ogive Curve Drawing & Median from N/2'}]}]}, {'day': 2, 'title_en': 'Day 2: Algebra Powerhouse (22+ Marks)', 'title_te': 'రెండో రోజు: బీజగణితం పవర్ హౌస్ (22+ మార్కులు)', 'theme_en': 'Polynomials, Linear Equations & Quadratic Equations', 'theme_te': 'బహుపదులు, రేఖీయ సమీకరణాలు & వర్గ సమీకరణాలు', 'target_marks': '22 - 26 Marks', 'chapters': [{'id': 3, 'name_en': 'Polynomials', 'name_te': 'బహుపదులు', 'weightage': '6 - 8 Marks', 'questions': [{'id': 'D2-C3-Q1', 'marks': '1 Mark', 'q_en': 'Find the zero of linear polynomial p(x) = 3x - 5.', 'q_te': 'p(x) = 3x - 5 రేఖీయ బహుపది శూన్యాన్ని కనుగొనండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Linear Zero: x = -b/a'}, {'id': 'D2-C3-Q2', 'marks': '1 Mark', 'q_en': 'If α and β are zeroes of 2x^2 + 5x - 7, find α + β and α*β.', 'q_te': '2x^2 + 5x - 7 బహుపది శూన్యాలు α, β అయితే α + β మరియు α*β విలువలను రాయండి.', 'trend': 'TS 2024 (Section I)', 'concept': 'Sum: -b/a, Product: c/a'}, {'id': 'D2-C3-Q3', 'marks': '2 Marks', 'q_en': 'Find a quadratic polynomial whose sum and product of zeroes are -3 and 2 respectively.', 'q_te': 'శూన్యాల మొత్తం -3 మరియు లబ్దం 2 గా గల వర్గ బహుపదిని కనుగొనండి.', 'trend': 'AP 2023, TS 2022 (Ex 3.3)', 'concept': 'p(x) = k[x^2 - (α+β)x + αβ]'}, {'id': 'D2-C3-Q4', 'marks': '2 Marks', 'q_en': 'Find the zeroes of p(x) = x^2 - 3 and verify relation between zeroes and coefficients.', 'q_te': 'p(x) = x^2 - 3 బహుపది శూన్యాలు కనుగొని, గుణకాలతో సంబంధాన్ని సరిచూడండి.', 'trend': 'TS 2023 (Ex 3.3 Q1)', 'concept': 'Difference of Squares Factorization'}, {'id': 'D2-C3-Q5', 'marks': '2 Marks', 'q_en': 'Check whether -2 and 2 are zeroes of the polynomial p(x) = x^4 - 16.', 'q_te': '-2 మరియు 2 లు p(x) = x^4 - 16 బహుపది శూన్యాలు అవుతాయో కాదో సరిచూడండి.', 'trend': 'AP 2024', 'concept': 'Remainder Theorem / Zero Check'}, {'id': 'D2-C3-Q6', 'marks': '4 Marks', 'q_en': 'Find the zeroes of quadratic polynomial p(x) = x^2 - 2x - 8 and verify the relationship between zeroes and coefficients.', 'q_te': 'x^2 - 2x - 8 బహుపది శూన్యాలు కనుగొని, శూన్యాలకు మరియు గుణకాలకు మధ్య గల సంబంధాన్ని సరిచూడండి.', 'trend': 'TS & AP Most Repeated (Ex 3.3 Q1)', 'concept': 'Zeroes & Coefficients Verification'}, {'id': 'D2-C3-Q7', 'marks': '4 Marks', 'q_en': 'Find a quadratic polynomial whose zeroes are 2 and -1/3.', 'q_te': '2 మరియు -1/3 శూన్యాలుగా గల వర్గ బహుపదిని కనుగొనండి.', 'trend': 'TS 2024, AP 2023', 'concept': 'Forming Polynomial from Roots'}, {'id': 'D2-C3-Q8', 'marks': '4 Marks', 'q_en': 'Divide 3x^3 + x^2 + 2x + 5 by 1 + 2x + x^2 and find quotient and remainder.', 'q_te': '3x^3 + x^2 + 2x + 5 ను x^2 + 2x + 1 చే భాగించి భాగఫలం మరియు శేషం కనుగొనండి.', 'trend': 'AP 2022 (Ex 3.4)', 'concept': 'Polynomial Long Division'}, {'id': 'D2-C3-Q9', 'marks': '8 Marks', 'q_en': 'Draw the graph of polynomial p(x) = x^2 - x - 6 and find its zeroes from the graph.', 'q_te': 'p(x) = x^2 - x - 6 వర్గ బహుపదికి గ్రాఫ్ గీసి, శూన్యాలను కనుగొనండి.', 'trend': 'TS 2024, AP 2024 Guaranteed 8M (Ex 3.2 Graph)', 'concept': 'Parabola Graphing & Zeroes at X-axis'}, {'id': 'D2-C3-Q10', 'marks': '8 Marks', 'q_en': 'Find all the zeroes of 2x^4 - 3x^3 - 3x^2 + 6x - 2, if you know that two of its zeroes are √2 and -√2.', 'q_te': '√2 మరియు -√2 లు శూన్యాలైతే 2x^4 - 3x^3 - 3x^2 + 6x - 2 యొక్క మిగిలిన అన్ని శూన్యాలను కనుగొనండి.', 'trend': 'AP 2023 (Section IV)', 'concept': 'Finding Remaining Roots of Degree 4'}]}, {'id': 4, 'name_en': 'Pair of Linear Equations in Two Variables', 'name_te': 'రెండు చరరాశులలో రేఖీయ సమీకరణాల జత', 'weightage': '6 - 8 Marks', 'questions': [{'id': 'D2-C4-Q1', 'marks': '1 Mark', 'q_en': 'Write the condition for a pair of linear equations a1x + b1y + c1 = 0 and a2x + b2y + c2 = 0 to be consistent with unique solution.', 'q_te': 'రెండు చరరాశులలో రేఖీయ సమీకరణాలు ఏకైక సాధన కలిగి ఉండటానికి నియమాన్ని రాయండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'a1/a2 ≠ b1/b2'}, {'id': 'D2-C4-Q2', 'marks': '1 Mark', 'q_en': 'For what value of k will the equations x + 2y = 3 and 5x + ky = 7 have no solution?', 'q_te': 'k యొక్క ఏ విలువకు x + 2y = 3 మరియు 5x + ky = 7 లకు సాధన ఉండదు?', 'trend': 'TS 2024', 'concept': 'Parallel Lines: a1/a2 = b1/b2 ≠ c1/c2'}, {'id': 'D2-C4-Q3', 'marks': '2 Marks', 'q_en': 'Check whether the pair of equations 2x + 3y = 8 and 4x + 6y = 7 is consistent or inconsistent.', 'q_te': '2x + 3y = 8 మరియు 4x + 6y = 7 సమీకరణాల జత సంగతమో లేదా అసంగతమో తెలపండి.', 'trend': 'AP 2023 (Ex 4.1)', 'concept': 'Ratio Comparison of Coefficients'}, {'id': 'D2-C4-Q4', 'marks': '2 Marks', 'q_en': 'Solve by substitution: x + y = 14 and x - y = 4.', 'q_te': 'ప్రతిక్షేపణ పద్ధతి ద్వారా సాధించండి: x + y = 14 మరియు x - y = 4.', 'trend': 'TS 2022', 'concept': 'Substitution Method'}, {'id': 'D2-C4-Q5', 'marks': '2 Marks', 'q_en': 'Solve by elimination: 2x + y = 10 and 3x - y = 5.', 'q_te': 'చరరాశిని తొలగించే పద్ధతి ద్వారా సాధించండి: 2x + y = 10 మరియు 3x - y = 5.', 'trend': 'AP 2024', 'concept': 'Elimination Method'}, {'id': 'D2-C4-Q6', 'marks': '4 Marks', 'q_en': 'Solve the pair of equations: 3x + 4y = 10 and 2x - 2y = 2 using elimination method.', 'q_te': '3x + 4y = 10 మరియు 2x - 2y = 2 లను ఎలిమినేషన్ పద్ధతిలో సాధించండి.', 'trend': 'TS 2023 (Ex 4.2 Q1)', 'concept': 'Standard Elimination Steps'}, {'id': 'D2-C4-Q7', 'marks': '4 Marks', 'q_en': 'The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.', 'q_te': 'రెండు సంపూరక కోణాలలో పెద్ద కోణం, చిన్న కోణం కంటే 18° ఎక్కువ. ఆ కోణాలను కనుగొనండి.', 'trend': 'AP 2023 (Ex 4.2 Q2)', 'concept': 'Supplementary Angle Word Problem'}, {'id': 'D2-C4-Q8', 'marks': '4 Marks', 'q_en': 'Solve the reducible equations: 2/√x + 3/√y = 2 and 4/√x - 9/√y = -1.', 'q_te': '2/√x + 3/√y = 2 మరియు 4/√x - 9/√y = -1 రేఖీయ రూపంలోకి మార్చి సాధించండి.', 'trend': 'TS 2024 (Ex 4.3)', 'concept': 'Equations Reducible to Linear Form'}, {'id': 'D2-C4-Q9', 'marks': '8 Marks', 'q_en': 'Solve graphically: 2x + y - 6 = 0 and 4x - 2y - 4 = 0. Find the area of triangle formed by these lines with y-axis.', 'q_te': 'గ్రాఫ్ పద్ధతిలో సాధించండి: 2x + y - 6 = 0 మరియు 4x - 2y - 4 = 0. ఈ రేఖలు y-అక్షంతో ఏర్పరచే త్రిభుజ వైశాల్యం కనుగొనండి.', 'trend': 'TS & AP Guaranteed 8M (Graph Question)', 'concept': 'Graphical Solution & Triangle Area'}, {'id': 'D2-C4-Q10', 'marks': '8 Marks', 'q_en': 'A boat goes 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it can go 40 km upstream and 55 km downstream. Find speed of stream and boat in still water.', 'q_te': 'ఒక పడవ ప్రవాహానికి ఎదురుగా 30 కి.మీ, ప్రవాహ దిశలో 44 కి.మీ దూరాన్ని 10 గంటల్లో ప్రయాణిస్తుంది... నిశ్చల నీటిలో పడవ వేగం, ప్రవాహ వేగం కనుగొనండి.', 'trend': 'AP 2024, TS 2023 (Ex 4.3 Q2 - 8M)', 'concept': 'Upstream / Downstream Speed Problem'}]}, {'id': 5, 'name_en': 'Quadratic Equations', 'name_te': 'వర్గ సమీకరణాలు', 'weightage': '6 - 8 Marks', 'questions': [{'id': 'D2-C5-Q1', 'marks': '1 Mark', 'q_en': 'Write the quadratic formula to find roots of ax^2 + bx + c = 0.', 'q_te': 'ax^2 + bx + c = 0 వర్గ సమీకరణం మూలాలు కనుగొనే వర్గ సూత్రం రాయండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Quadratic Formula: [-b ± √(b^2-4ac)] / 2a'}, {'id': 'D2-C5-Q2', 'marks': '1 Mark', 'q_en': 'Find the discriminant of quadratic equation 2x^2 - 4x + 3 = 0 and state nature of roots.', 'q_te': '2x^2 - 4x + 3 = 0 సమీకరణం విచక్షణి కనుగొని, మూలాల స్వభావాన్ని తెలపండి.', 'trend': 'TS 2024', 'concept': 'D = b^2 - 4ac < 0 (No real roots)'}, {'id': 'D2-C5-Q3', 'marks': '2 Marks', 'q_en': 'Find the value of k for which 2x^2 + kx + 3 = 0 has two equal real roots.', 'q_te': '2x^2 + kx + 3 = 0 సమీకరణానికి సమాన వాస్తవ మూలాలుంటే k విలువ కనుగొనండి.', 'trend': 'AP 2023, TS 2022 (Ex 5.4)', 'concept': 'Equal Roots: b^2 - 4ac = 0'}, {'id': 'D2-C5-Q4', 'marks': '2 Marks', 'q_en': 'Solve by factorisation: x^2 - 3x - 10 = 0.', 'q_te': 'కారణాంకాల పద్ధతి ద్వారా సాధించండి: x^2 - 3x - 10 = 0.', 'trend': 'TS 2023 (Ex 5.2 Q1)', 'concept': 'Factoring by Splitting Middle Term'}, {'id': 'D2-C5-Q5', 'marks': '2 Marks', 'q_en': 'Solve: √2 x^2 + 7x + 5√2 = 0 by factorisation.', 'q_te': 'కారణాంకాల పద్ధతిలో సాధించండి: √2 x^2 + 7x + 5√2 = 0.', 'trend': 'AP 2024, TS 2024 (Ex 5.2)', 'concept': 'Irrational Coefficient Factoring'}, {'id': 'D2-C5-Q6', 'marks': '4 Marks', 'q_en': 'Find two consecutive positive integers, sum of whose squares is 365.', 'q_te': 'రెండు వరుస ధన పూర్ణసంఖ్యల వర్గాల మొత్తం 365 అయితే ఆ సంఖ్యలను కనుగొనండి.', 'trend': 'TS 2023 (Ex 5.2 Q4)', 'concept': 'Quadratic Word Problem'}, {'id': 'D2-C5-Q7', 'marks': '4 Marks', 'q_en': 'Find the roots of 2x^2 - 7x + 3 = 0 by method of completing the square.', 'q_te': 'వర్గాన్ని పూర్తి చేసే పద్ధతి ద్వారా 2x^2 - 7x + 3 = 0 మూలాలను కనుగొనండి.', 'trend': 'AP 2023 (Ex 5.3)', 'concept': 'Completing the Square Method'}, {'id': 'D2-C5-Q8', 'marks': '4 Marks', 'q_en': 'Find the roots of quadratic equation 5x^2 - 6x - 2 = 0 using the quadratic formula.', 'q_te': 'వర్గ సూత్రం ఉపయోగించి 5x^2 - 6x - 2 = 0 మూలాలను కనుగొనండి.', 'trend': 'TS 2024 (Ex 5.3)', 'concept': 'Application of Quadratic Formula'}, {'id': 'D2-C5-Q9', 'marks': '8 Marks', 'q_en': 'An express train takes 1 hour less than a passenger train to travel 132 km between Mysore and Bangalore. If average speed of express train is 11 km/h more than passenger train, find speeds of both.', 'q_te': '132 కి.మీ దూరం ప్రయాణించడానికి ఎక్స్\u200cప్రెస్ రైలు, ప్యాసింజర్ రైలు కంటే 1 గంట తక్కువ సమయం తీసుకుంటుంది... రెండు రైళ్ళ సగటు వేగాలను కనుగొనండి.', 'trend': 'TS & AP Most Repeated 8M (Ex 5.3 Q10)', 'concept': 'Speed, Distance & Quadratic Modelling'}, {'id': 'D2-C5-Q10', 'marks': '8 Marks', 'q_en': 'Two water taps together can fill a tank in 9 3/8 hours. The tap of larger diameter takes 10 hours less than smaller one to fill tank separately. Find time taken by each tap.', 'q_te': 'రెండు కుళాయిలు కలిసి ఒక తొట్టెను 9 3/8 గంటల్లో నింపగలవు. పెద్ద వ్యాసం గల కుళాయి విడిగా 10 గంటలు తక్కువ సమయం తీసుకుంటుంది... ఒక్కొక్క కుళాయి పట్టే సమయం కనుగొనండి.', 'trend': 'AP 2024, TS 2023 (Ex 5.3 Q9)', 'concept': 'Work & Time Quadratic Formulation'}]}]}, {'day': 3, 'title_en': 'Day 3: Progressions & Coordinate Geometry (16+ Marks)', 'title_te': 'మూడో రోజు: శ్రేఢులు & నిరూపక జ్యామితి (16+ మార్కులు)', 'theme_en': 'Arithmetic & Geometric Progressions, Coordinate Geometry', 'theme_te': 'అంకశ్రేఢి, గుణశ్రేఢి & నిరూపక రేఖాగణితం', 'target_marks': '16 - 20 Marks', 'chapters': [{'id': 6, 'name_en': 'Progressions', 'name_te': 'శ్రేఢులు', 'weightage': '8 Marks', 'questions': [{'id': 'D3-C6-Q1', 'marks': '1 Mark', 'q_en': 'Write the general formula for n-th term of an Arithmetic Progression (AP) and define terms.', 'q_te': 'అంకశ్రేఢి (AP) n-వ పదం సూత్రం రాసి, పదాలను వివరించండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'an = a + (n - 1)d'}, {'id': 'D3-C6-Q2', 'marks': '1 Mark', 'q_en': 'Find the 10th term of the AP: 2, 7, 12, ...', 'q_te': '2, 7, 12, ... అంకశ్రేఢిలో 10వ పదాన్ని కనుగొనండి.', 'trend': 'TS 2024 (Ex 6.2 Q2)', 'concept': 'Direct an computation'}, {'id': 'D3-C6-Q3', 'marks': '2 Marks', 'q_en': 'Which term of the AP: 3, 8, 13, 18, ... is 78?', 'q_te': '3, 8, 13, 18, ... అంకశ్రేఢిలో ఎన్నవ పదం 78 అవుతుంది?', 'trend': 'AP 2023 (Ex 6.2 Q4)', 'concept': 'Finding n when an is given'}, {'id': 'D3-C6-Q4', 'marks': '2 Marks', 'q_en': 'Find the sum of first 20 terms of the AP: 1, 4, 7, 10, ...', 'q_te': '1, 4, 7, 10, ... అంకశ్రేఢిలోని మొదటి 20 పదాల మొత్తం కనుగొనండి.', 'trend': 'TS 2022 (Ex 6.3)', 'concept': 'Sn = n/2 [2a + (n-1)d]'}, {'id': 'D3-C6-Q5', 'marks': '2 Marks', 'q_en': 'Find the 8th term of the GP: 2, 6, 18, 54, ...', 'q_te': '2, 6, 18, 54, ... గుణశ్రేఢి (GP) లో 8వ పదాన్ని కనుగొనండి.', 'trend': 'AP 2024 (Ex 6.4)', 'concept': 'GP n-th term: an = a * r^(n-1)'}, {'id': 'D3-C6-Q6', 'marks': '4 Marks', 'q_en': 'In an AP, if the 3rd term is 5 and 7th term is 9, find the AP and its 12th term.', 'q_te': 'ఒక అంకశ్రేఢిలో 3వ పదం 5, 7వ పదం 9 అయితే ఆ అంకశ్రేఢిని మరియు 12వ పదాన్ని కనుగొనండి.', 'trend': 'TS 2023 (Ex 6.2 Q3)', 'concept': 'Linear System from AP Terms'}, {'id': 'D3-C6-Q7', 'marks': '4 Marks', 'q_en': 'How many multiples of 4 lie between 10 and 250?', 'q_te': '10 మరియు 250 ల మధ్య గల 4 యొక్క గుణిజాలు ఎన్ని?', 'trend': 'AP 2024, TS 2023 (Ex 6.2 Q13)', 'concept': 'AP Count of Multiples'}, {'id': 'D3-C6-Q8', 'marks': '4 Marks', 'q_en': 'Find the sum of first 14 terms of an AP whose 2nd and 3rd terms are 14 and 18 respectively.', 'q_te': 'ఒక అంకశ్రేఢి 2వ మరియు 3వ పదాలు వరుసగా 14, 18 అయితే మొదటి 14 పదాల మొత్తం కనుగొనండి.', 'trend': 'TS 2024 (Ex 6.3 Q7)', 'concept': 'Sum of First n Terms'}, {'id': 'D3-C6-Q9', 'marks': '8 Marks', 'q_en': 'If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms.', 'q_te': 'ఒక అంకశ్రేఢి మొదటి 7 పదాల మొత్తం 49, మరియు మొదటి 17 పదాల మొత్తం 289 అయితే మొదటి n పదాల మొత్తం కనుగొనండి.', 'trend': 'TS & AP Most Repeated 8M (Ex 6.3 Q9)', 'concept': 'Sn Formula System & Derivation of n^2'}, {'id': 'D3-C6-Q10', 'marks': '8 Marks', 'q_en': 'A manufacturer of TV sets produced 600 sets in the third year and 700 sets in the seventh year. Assuming production increases uniformly by a fixed number every year, find: (i) production in 1st year (ii) production in 10th year (iii) total production in first 7 years.', 'q_te': 'ఒక టీవీల తయారీ కంపెనీ 3వ సంవత్సరంలో 600 టీవీలు, 7వ సంవత్సరంలో 700 టీవీలు తయారు చేస్తే: (i) మొదటి సంవత్సరం (ii) 10వ సంవత్సరం (iii) మొదటి 7 సంవత్సరాల మొత్తం ఉత్పత్తి కనుగొనండి.', 'trend': 'AP 2024 (Section IV 8M)', 'concept': 'Real-Life AP Word Application'}]}, {'id': 7, 'name_en': 'Coordinate Geometry', 'name_te': 'నిరూపక రేఖాగణితం', 'weightage': '8 Marks', 'questions': [{'id': 'D3-C7-Q1', 'marks': '1 Mark', 'q_en': 'Find the distance of point P(3, 4) from the origin (0, 0).', 'q_te': 'మూలబిందువు (0, 0) నుండి P(3, 4) బిందువుకు గల దూరం ఎంత?', 'trend': 'TS 2023, AP 2024', 'concept': 'Distance from Origin: √(x^2 + y^2)'}, {'id': 'D3-C7-Q2', 'marks': '1 Mark', 'q_en': 'Find the midpoint of the line segment joining points A(2, 7) and B(12, -7).', 'q_te': 'A(2, 7) మరియు B(12, -7) బిందువులను కలిపే రేఖాఖండం మధ్యబిందువును కనుగొనండి.', 'trend': 'TS 2024', 'concept': 'Midpoint: ((x1+x2)/2, (y1+y2)/2)'}, {'id': 'D3-C7-Q3', 'marks': '2 Marks', 'q_en': 'Find the distance between the points (-5, 7) and (-1, 3).', 'q_te': '(-5, 7) మరియు (-1, 3) బిందువుల మధ్య దూరాన్ని కనుగొనండి.', 'trend': 'AP 2023, TS 2022 (Ex 7.1 Q1)', 'concept': 'Distance Formula: √((x2-x1)^2 + (y2-y1)^2)'}, {'id': 'D3-C7-Q4', 'marks': '2 Marks', 'q_en': 'Find the coordinates of the point which divides the line segment joining (4, -3) and (8, 5) in the ratio 3 : 1 internally.', 'q_te': '(4, -3) మరియు (8, 5) బిందువులను కలిపే రేఖాఖండాన్ని 3 : 1 నిష్పత్తిలో అంతరంగా విభజించే బిందువు నిరూపకాలు కనుగొనండి.', 'trend': 'TS 2023 (Ex 7.2 Q1)', 'concept': 'Section Formula'}, {'id': 'D3-C7-Q5', 'marks': '2 Marks', 'q_en': 'Find the centroid of the triangle whose vertices are (-4, 6), (2, -2) and (2, 5).', 'q_te': '(-4, 6), (2, -2) మరియు (2, 5) శీర్షాలుగా గల త్రిభుజ గురుత్వ కేంద్రాన్ని (Centroid) కనుగొనండి.', 'trend': 'AP 2024', 'concept': 'Centroid: ((x1+x2+x3)/3, (y1+y2+y3)/3)'}, {'id': 'D3-C7-Q6', 'marks': '4 Marks', 'q_en': 'Check whether the points (1, 5), (2, 3) and (-2, -11) are collinear.', 'q_te': '(1, 5), (2, 3) మరియు (-2, -11) బిందువులు సరేఖీయాలు అవుతాయో కాదో పరిశీలించండి.', 'trend': 'TS 2023, AP 2023 (Ex 7.1 Q3)', 'concept': 'Collinearity via Distance or Area = 0'}, {'id': 'D3-C7-Q7', 'marks': '4 Marks', 'q_en': 'Find a relation between x and y such that the point (x, y) is equidistant from the points (3, 6) and (-3, 4).', 'q_te': '(x, y) బిందువు (3, 6) మరియు (-3, 4) బిందువుల నుండి సమాన దూరంలో ఉంటే x, y ల మధ్య సంబంధాన్ని కనుగొనండి.', 'trend': 'TS 2024 (Ex 7.1 Q10)', 'concept': 'Equidistant Locus / Perpendicular Bisector'}, {'id': 'D3-C7-Q8', 'marks': '4 Marks', 'q_en': 'Find the area of the triangle whose vertices are (2, 3), (-1, 0) and (2, -4).', 'q_te': '(2, 3), (-1, 0) మరియు (2, -4) శీర్షాలుగా గల త్రిభుజ వైశాల్యాన్ని కనుగొనండి.', 'trend': 'AP 2023 (Ex 7.3 Q1)', 'concept': 'Area = 1/2 |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|'}, {'id': 'D3-C7-Q9', 'marks': '8 Marks', 'q_en': 'Find the coordinates of the points of trisection of the line segment joining (2, -2) and (-7, 4).', 'q_te': '(2, -2) మరియు (-7, 4) లను కలిపే రేఖాఖండాన్ని సమత్రిఖండన చేసే బిందువుల నిరూపకాలను కనుగొనండి.', 'trend': 'TS & AP Most Repeated 8M (Ex 7.2 Q2)', 'concept': 'Trisection Points (1:2 and 2:1 Ratios)'}, {'id': 'D3-C7-Q10', 'marks': '8 Marks', 'q_en': 'Find the area of quadrilateral whose vertices taken in order are (-4, -2), (-3, -5), (3, -2) and (2, 3).', 'q_te': 'వరుసగా (-4, -2), (-3, -5), (3, -2) మరియు (2, 3) శీర్షాలుగా గల చతుర్భుజ వైశాల్యాన్ని కనుగొనండి.', 'trend': 'AP 2024, TS 2023 (Ex 7.3 Q4 - 8M)', 'concept': 'Quadrilateral Area by Splitting 2 Triangles'}]}]}, {'day': 4, 'title_en': 'Day 4: Geometry & Mensuration Mastery (20+ Marks)', 'title_te': 'నాల్గో రోజు: జ్యామితి & క్షేత్రమితి మాస్టరీ (20+ మార్కులు)', 'theme_en': 'Similar Triangles, Tangents & Secants, Mensuration', 'theme_te': 'సరూప త్రిభుజాలు, స్పర్శరేఖలు & ఛేదనరేఖలు, క్షేత్రమితి', 'target_marks': '20 - 24 Marks', 'chapters': [{'id': 8, 'name_en': 'Similar Triangles', 'name_te': 'సరూప త్రిభుజాలు', 'weightage': '8 Marks', 'questions': [{'id': 'D4-C8-Q1', 'marks': '1 Mark', 'q_en': 'State Basic Proportionality Theorem (Thales Theorem).', 'q_te': 'ప్రాథమిక అనుపాత సిద్ధాంతం (థేల్స్ సిద్ధాంతం) నిర్వచించండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Thales Theorem Statement'}, {'id': 'D4-C8-Q2', 'marks': '1 Mark', 'q_en': 'State Pythagoras Theorem.', 'q_te': 'పైథాగరస్ సిద్ధాంతాన్ని తెలపండి.', 'trend': 'TS 2024, AP 2023', 'concept': 'Hypotenuse^2 = Base^2 + Height^2'}, {'id': 'D4-C8-Q3', 'marks': '2 Marks', 'q_en': 'In ΔABC, DE || BC. If AD = 1.5 cm, DB = 3 cm, and AE = 1 cm, find EC.', 'q_te': 'ΔABC లో DE || BC. AD = 1.5 సెం.మీ, DB = 3 సెం.మీ, AE = 1 సెం.మీ అయితే EC ని కనుగొనండి.', 'trend': 'TS 2023 (Ex 8.1 Q1)', 'concept': 'AD/DB = AE/EC Application'}, {'id': 'D4-C8-Q4', 'marks': '2 Marks', 'q_en': 'A vertical pole of length 6 m casts a shadow 4 m long on ground. At same time a tower casts shadow 28 m long. Find height of tower.', 'q_te': '6 మీ. పొడవు గల స్తంభం 4 మీ. నీడను ఏర్పరచిన అదే సమయంలో ఒక టవర్ 28 మీ. నీడను ఏర్పరిస్తే టవర్ ఎత్తు ఎంత?', 'trend': 'AP 2023 (Ex 8.2 Q6)', 'concept': 'Similar Triangle Shadow Proportion'}, {'id': 'D4-C8-Q5', 'marks': '2 Marks', 'q_en': 'The areas of two similar triangles are 64 cm^2 and 121 cm^2. If EF = 15.4 cm, find BC.', 'q_te': 'రెండు సరూప త్రిభుజాల వైశాల్యాలు 64 సెం.మీ^2, 121 సెం.మీ^2. EF = 15.4 సెం.మీ అయితే BC కనుగొనండి.', 'trend': 'TS 2022 (Ex 8.3)', 'concept': 'Ratio of Areas = Ratio of Squares of Sides'}, {'id': 'D4-C8-Q6', 'marks': '4 Marks', 'q_en': 'A ladder 10 m long reaches a window 8 m above ground. Find distance of foot of ladder from base of wall.', 'q_te': '10 మీ. పొడవు గల నిచ్చెన నేల నుండి 8 మీ. ఎత్తులోని కిటికీని తాకితే నిచ్చెన అడుగు గోడ నుండి ఎంత దూరంలో ఉంది?', 'trend': 'TS 2024, AP 2024 (Ex 8.4 Q1)', 'concept': 'Pythagoras Application'}, {'id': 'D4-C8-Q7', 'marks': '4 Marks', 'q_en': 'Prove that if a line is drawn parallel to one side of a triangle intersecting other two sides, it divides them in the same ratio.', 'q_te': 'త్రిభుజంలో ఒక భుజానికి సమాంతరంగా గీసిన సరళరేఖ మిగిలిన రెండు భుజాలను సమాన నిష్పత్తిలో విభజిస్తుందని నిరూపించండి.', 'trend': 'TS & AP Most Famous Theorem', 'concept': 'Basic Proportionality Theorem Proof'}, {'id': 'D4-C8-Q8', 'marks': '4 Marks', 'q_en': 'In ΔABC, ∠B = 90° and D is midpoint of BC. Prove that AC^2 = 4AD^2 - 3AB^2.', 'q_te': 'ΔABC లో ∠B = 90° మరియు BC కి D మధ్యబిందువైతే, AC^2 = 4AD^2 - 3AB^2 అని నిరూపించండి.', 'trend': 'AP 2023 (Section III)', 'concept': 'Pythagoras Geometric Deduction'}, {'id': 'D4-C8-Q9', 'marks': '8 Marks', 'q_en': 'State and prove Pythagoras Theorem.', 'q_te': 'పైథాగరస్ సిద్ధాంతాన్ని ప్రవచించి, నిరూపించండి.', 'trend': 'TS 2024, AP 2023 Guaranteed 8M Theorem', 'concept': 'Full Pythagoras Formal Proof'}, {'id': 'D4-C8-Q10', 'marks': '8 Marks', 'q_en': 'Construct a triangle of sides 4 cm, 5 cm and 6 cm and then a triangle similar to it whose sides are 2/3 of corresponding sides of first triangle.', 'q_te': '4 సెం.మీ, 5 సెం.మీ, 6 సెం.మీ భుజాలుగా గల త్రిభుజం నిర్మించి, దానికి 2/3 స్కేల్ గుణకం గల సరూప త్రిభుజాన్ని నిర్మించండి.', 'trend': 'TS & AP Compulsory 8M Construction (Ex 8.2)', 'concept': 'Scale Factor Triangle Construction'}]}, {'id': 9, 'name_en': 'Tangents and Secants to a Circle', 'name_te': 'వృత్తానికి స్పర్శరేఖలు మరియు ఛేదనరేఖలు', 'weightage': '6 Marks', 'questions': [{'id': 'D4-C9-Q1', 'marks': '1 Mark', 'q_en': 'How many tangents can be drawn to a circle from an external point?', 'q_te': 'వృత్త బాహ్య బిందువు నుండి వృత్తానికి ఎన్ని స్పర్శరేఖలు గీయవచ్చు?', 'trend': 'TS 2023, AP 2024', 'concept': 'Exactly 2 Tangents'}, {'id': 'D4-C9-Q2', 'marks': '1 Mark', 'q_en': 'What is the angle between tangent and radius through point of contact?', 'q_te': 'స్పర్శ బిందువు వద్ద గీసిన వ్యాసార్థానికి మరియు స్పర్శరేఖకు మధ్య కోణం ఎంత?', 'trend': 'TS 2024', 'concept': '90 degrees (Perpendicularity)'}, {'id': 'D4-C9-Q3', 'marks': '2 Marks', 'q_en': 'A tangent PQ at point P of circle of radius 5 cm meets a line through center O at Q so that OQ = 12 cm. Find length of PQ.', 'q_te': '5 సెం.మీ వ్యాసార్థం గల వృత్తానికి P వద్ద గీసిన స్పర్శరేఖ PQ... OQ = 12 సెం.మీ అయితే PQ పొడవు కనుగొనండి.', 'trend': 'AP 2023 (Ex 9.1 Q3)', 'concept': 'PQ = √(OQ^2 - OP^2)'}, {'id': 'D4-C9-Q4', 'marks': '2 Marks', 'q_en': 'If tangents PA and PB from a point P to a circle with center O are inclined to each other at angle of 80°, find ∠POA.', 'q_te': 'వృత్తానికి P నుండి గీసిన PA, PB స్పర్శరేఖల మధ్య కోణం 80° అయితే ∠POA ని కనుగొనండి.', 'trend': 'TS 2023 (Ex 9.2 Q3)', 'concept': 'Supplementary Tangent Angles'}, {'id': 'D4-C9-Q5', 'marks': '2 Marks', 'q_en': 'Find the area of sector of circle with radius 6 cm if angle of sector is 60°.', 'q_te': '6 సెం.మీ వ్యాసార్థం, 60° సెక్టార్ కోణం గల వృత్త సెక్టార్ వైశాల్యాన్ని కనుగొనండి.', 'trend': 'AP 2024 (Ex 9.3 Q1)', 'concept': 'Sector Area: (x/360) * π*r^2'}, {'id': 'D4-C9-Q6', 'marks': '4 Marks', 'q_en': 'Prove that the lengths of tangents drawn from an external point to a circle are equal.', 'q_te': 'బాహ్య బిందువు నుండి వృత్తానికి గీసిన స్పర్శరేఖల పొడవులు సమానమని నిరూపించండి.', 'trend': 'TS & AP Most Repeated Theorem (Theorem 9.2)', 'concept': 'Tangents from External Point Equal Proof'}, {'id': 'D4-C9-Q7', 'marks': '4 Marks', 'q_en': 'A quadrilateral ABCD is drawn to circumscribe a circle. Prove that AB + CD = AD + BC.', 'q_te': 'ఒక వృత్తాన్ని పరివృత్తం చేస్తూ చతుర్భుజం ABCD గీయబడింది. AB + CD = AD + BC అని చూపండి.', 'trend': 'TS 2024, AP 2023 (Ex 9.2 Q8)', 'concept': 'Circumscribed Quadrilateral Sides'}, {'id': 'D4-C9-Q8', 'marks': '4 Marks', 'q_en': 'Find the area of the shaded region if ABCD is a square of side 14 cm and APD and BPC are semicircles.', 'q_te': '14 సెం.మీ భుజం గల చతురస్రం ABCD లో APD, BPC లు అర్ధవృత్తాలైతే షేడ్ చేసిన ప్రాంత వైశాల్యం కనుగొనండి.', 'trend': 'TS 2023 (Ex 9.3 Q3)', 'concept': 'Square - 2 Semicircles Combination'}, {'id': 'D4-C9-Q9', 'marks': '8 Marks', 'q_en': 'Draw a circle of radius 6 cm. From a point 10 cm away from its centre, construct the pair of tangents to the circle and measure their lengths.', 'q_te': '6 సెం.మీ వ్యాసార్థం గల వృత్తాన్ని గీయండి. కేంద్రం నుండి 10 సెం.మీ దూరంలో ఉన్న బిందువు నుండి స్పర్శరేఖల జతను నిర్మించి, వాటి పొడవులను కొలవండి.', 'trend': 'TS & AP Guaranteed 8M Construction (Ex 9.2)', 'concept': 'Pair of Tangents Construction by Perpendicular Bisector'}, {'id': 'D4-C9-Q10', 'marks': '8 Marks', 'q_en': 'A chord of circle of radius 15 cm subtends angle of 60° at centre. Find areas of corresponding minor and major segments of circle. (Use π = 3.14, √3 = 1.73)', 'q_te': '15 సెం.మీ వ్యాసార్థం గల వృత్తంలో ఒక జ్యా కేంద్రం వద్ద 60° కోణం చేస్తే అల్ప, అధిక వృత్తఖండాల వైశాల్యాలను కనుగొనండి.', 'trend': 'AP 2024, TS 2023 (Ex 9.3)', 'concept': 'Segment Area = Sector Area - Triangle Area'}]}, {'id': 10, 'name_en': 'Mensuration', 'name_te': 'క్షేత్రమితి', 'weightage': '8 - 10 Marks', 'questions': [{'id': 'D4-C10-Q1', 'marks': '1 Mark', 'q_en': 'Write the formula for Total Surface Area (TSA) of a cone with radius r and slant height l.', 'q_te': 'శంఖువు సంపూర్ణతల వైశాల్యం (TSA) సూత్రాన్ని రాయండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'TSA Cone = π*r*(l + r)'}, {'id': 'D4-C10-Q2', 'marks': '1 Mark', 'q_en': 'Find the volume of a sphere of radius 7 cm. (Take π = 22/7)', 'q_te': '7 సెం.మీ వ్యాసార్థం గల గోళం ఘనపరిమాణాన్ని కనుగొనండి.', 'trend': 'TS 2024', 'concept': 'Volume = 4/3 * π * r^3'}, {'id': 'D4-C10-Q3', 'marks': '2 Marks', 'q_en': '2 cubes each of volume 64 cm^3 are joined end to end. Find surface area of resulting cuboid.', 'q_te': 'ఒక్కొక్కటి 64 సెం.మీ^3 ఘనపరిమాణం గల రెండు సమఘనాలను కలిపితే ఏర్పడే దీర్ఘఘనం ఉపరితల వైశాల్యం కనుగొనండి.', 'trend': 'AP 2023, TS 2022 (Ex 10.1 Q1)', 'concept': 'Combination of Two Cubes'}, {'id': 'D4-C10-Q4', 'marks': '2 Marks', 'q_en': 'A cone of height 24 cm and radius of base 6 cm is made up of modelling clay. A child reshapes it into a sphere. Find radius of sphere.', 'q_te': '24 సెం.మీ ఎత్తు, 6 సెం.మీ వ్యాసార్థం గల మట్టి శంఖువును గోళంగా మారిస్తే ఆ గోళం వ్యాసార్థం కనుగొనండి.', 'trend': 'TS 2023 (Ex 10.3 Q2)', 'concept': 'Volume Equating during Reshaping'}, {'id': 'D4-C10-Q5', 'marks': '2 Marks', 'q_en': 'Find the slant height l of a cone if base radius is 7 cm and vertical height is 24 cm.', 'q_te': 'భూవ్యాసార్థం 7 సెం.మీ, ఎత్తు 24 సెం.మీ గల శంఖువు ఏటవాలు ఎత్తు (l) ను కనుగొనండి.', 'trend': 'AP 2024', 'concept': 'Slant Height: l = √(r^2 + h^2)'}, {'id': 'D4-C10-Q6', 'marks': '4 Marks', 'q_en': 'A toy is in the form of a cone of radius 3.5 cm mounted on a hemisphere of same radius. The total height of toy is 15.5 cm. Find total surface area of toy.', 'q_te': '3.5 సెం.మీ వ్యాసార్థం గల అర్ధగోళంపై అదే వ్యాసార్థం గల శంఖువు అమర్చిన ఒక బొమ్మ మొత్తం ఎత్తు 15.5 సెం.మీ అయితే దాని సంపూర్ణతల వైశాల్యం కనుగొనండి.', 'trend': 'TS & AP Most Repeated (Ex 10.1 Q3)', 'concept': 'TSA Toy = CSA Cone + CSA Hemisphere'}, {'id': 'D4-C10-Q7', 'marks': '4 Marks', 'q_en': 'A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. If total length is 14 mm and diameter is 5 mm, find its surface area.', 'q_te': 'ఒక ఔషధ క్యాప్సూల్ సిలిండర్ ఆకారంలో ఉండి, రెండు చివర్లా అర్ధగోళాలు కలిగి ఉంది... దాని ఉపరితల వైశాల్యం కనుగొనండి.', 'trend': 'TS 2024 (Ex 10.1 Q6)', 'concept': 'Cylinder + 2 Hemispheres Surface Area'}, {'id': 'D4-C10-Q8', 'marks': '4 Marks', 'q_en': 'A metallic sphere of radius 4.2 cm is melted and recast into shape of a cylinder of radius 6 cm. Find height of cylinder.', 'q_te': '4.2 సెం.మీ వ్యాసార్థం గల లోహపు గోళాన్ని కరిగించి 6 సెం.మీ వ్యాసార్థం గల స్తూపంగా మారిస్తే స్తూపం ఎత్తు కనుగొనండి.', 'trend': 'AP 2023 (Ex 10.3 Q1)', 'concept': 'Melting and Recasting: Volume Equality'}, {'id': 'D4-C10-Q9', 'marks': '8 Marks', 'q_en': 'A solid toy is in the form of a right circular cylinder with hemispherical shape at one end and a cone at other end. Their common diameter is 4.2 cm, height of cylindrical part is 12 cm and cone height is 7 cm. Find volume of toy.', 'q_te': 'ఒక వైపు అర్ధగోళం, మరోవైపు శంఖువు కలిగిన స్తూపాకార బొమ్మ... దాని మొత్తం ఘనపరిమాణాన్ని కనుగొనండి.', 'trend': 'TS 2024, AP 2024 (Section IV 8M)', 'concept': 'Combined Solid Volume (Cone + Cylinder + Hemisphere)'}, {'id': 'D4-C10-Q10', 'marks': '8 Marks', 'q_en': 'A well of diameter 3 m is dug 14 m deep. The earth taken out of it is spread evenly all around it in the shape of a circular ring of width 4 m to form an embankment. Find the height of the embankment.', 'q_te': '3 మీ. వ్యాసం గల బావిని 14 మీ. లోతు తవ్వి తీసిన మట్టితో 4 మీ. వెడల్పు గల గట్టును నిర్మిస్తే ఆ గట్టు ఎత్తును కనుగొనండి.', 'trend': 'TS & AP Most Famous 8M (Ex 10.3 Q4)', 'concept': 'Cylinder Well Volume = Hollow Cylinder Ring Volume'}]}]}, {'day': 5, 'title_en': 'Day 5: Trigonometry, Heights & Chance (18+ Marks)', 'title_te': 'ఐదో రోజు: త్రికోణమితి, ఎత్తులు & సంభావ్యత (18+ మార్కులు)', 'theme_en': 'Trigonometry, Applications of Trig & Probability', 'theme_te': 'త్రికోణమితి, త్రికోణమితి అనువర్తనాలు & సంభావ్యత', 'target_marks': '18 - 22 Marks', 'chapters': [{'id': 11, 'name_en': 'Trigonometry', 'name_te': 'త్రికోణమితి', 'weightage': '8 Marks', 'questions': [{'id': 'D5-C11-Q1', 'marks': '1 Mark', 'q_en': 'Evaluate: sin 30° + cos 60°.', 'q_te': 'sin 30° + cos 60° విలువను లెక్కించండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Standard Trigonometric Ratios Table'}, {'id': 'D5-C11-Q2', 'marks': '1 Mark', 'q_en': 'State the three fundamental trigonometric identities.', 'q_te': 'మూడు ప్రాథమిక త్రికోణమితి సర్వసమీకరణాలను రాయండి.', 'trend': 'TS 2024', 'concept': 'sin^2+cos^2=1, 1+tan^2=sec^2, 1+cot^2=cosec^2'}, {'id': 'D5-C11-Q3', 'marks': '2 Marks', 'q_en': 'In ΔABC right angled at B, AB = 24 cm, BC = 7 cm. Find sin A, cos A and sin C.', 'q_te': 'ΔABC లో ∠B = 90°, AB = 24 సెం.మీ, BC = 7 సెం.మీ అయితే sin A, cos A మరియు sin C కనుగొనండి.', 'trend': 'AP 2023, TS 2022 (Ex 11.1 Q1)', 'concept': 'Right Triangle Ratio Definitions'}, {'id': 'D5-C11-Q4', 'marks': '2 Marks', 'q_en': 'If tan A = 4/3, find the values of sin A and cos A.', 'q_te': 'tan A = 4/3 అయితే sin A మరియు cos A విలువలను కనుగొనండి.', 'trend': 'TS 2023 (Ex 11.1)', 'concept': 'Pythagorean Triplet (3, 4, 5)'}, {'id': 'D5-C11-Q5', 'marks': '2 Marks', 'q_en': 'Evaluate: (2 tan 30°) / (1 + tan^2 30°).', 'q_te': '(2 tan 30°) / (1 + tan^2 30°) విలువను కనుగొనండి.', 'trend': 'AP 2024 (Ex 11.2 Q2)', 'concept': 'Value Substitution (= sin 60°)'}, {'id': 'D5-C11-Q6', 'marks': '4 Marks', 'q_en': 'Prove that (sin θ + cosec θ)^2 + (cos θ + sec θ)^2 = 7 + tan^2 θ + cot^2 θ.', 'q_te': '(sin θ + cosec θ)^2 + (cos θ + sec θ)^2 = 7 + tan^2 θ + cot^2 θ అని నిరూపించండి.', 'trend': 'TS & AP Most Repeated (Ex 11.4 Q8)', 'concept': 'Algebraic Expansion + Trig Identities'}, {'id': 'D5-C11-Q7', 'marks': '4 Marks', 'q_en': 'Prove that √((1 + cos θ) / (1 - cos θ)) = cosec θ + cot θ.', 'q_te': '√((1 + cos θ) / (1 - cos θ)) = cosec θ + cot θ అని నిరూపించండి.', 'trend': 'TS 2024, AP 2023 (Ex 11.4 Q6)', 'concept': 'Conjugate Rationalization Proof'}, {'id': 'D5-C11-Q8', 'marks': '4 Marks', 'q_en': 'If cosec θ + cot θ = k, then prove that cos θ = (k^2 - 1) / (k^2 + 1).', 'q_te': 'cosec θ + cot θ = k అయితే cos θ = (k^2 - 1) / (k^2 + 1) అని చూపండి.', 'trend': 'AP 2024 (Ex 11.4 Q10)', 'concept': 'Identity Application (cosec^2 - cot^2 = 1)'}, {'id': 'D5-C11-Q9', 'marks': '8 Marks', 'q_en': 'Prove that: (tan θ / (1 - cot θ)) + (cot θ / (1 - tan θ)) = 1 + sec θ * cosec θ.', 'q_te': '(tan θ / (1 - cot θ)) + (cot θ / (1 - tan θ)) = 1 + sec θ * cosec θ అని నిరూపించండి.', 'trend': 'TS & AP Most Famous 8M Identity (Ex 11.4 Q3)', 'concept': 'Converting to sin and cos & LCM Simplification'}, {'id': 'D5-C11-Q10', 'marks': '8 Marks', 'q_en': 'If sec θ + tan θ = p, obtain values of sec θ, tan θ and sin θ in terms of p.', 'q_te': 'sec θ + tan θ = p అయితే p పదాలలో sec θ, tan θ మరియు sin θ విలువలను కనుగొనండి.', 'trend': 'TS 2023, AP 2024 (Section IV 8M)', 'concept': 'sec θ - tan θ = 1/p and System Solution'}]}, {'id': 12, 'name_en': 'Applications of Trigonometry', 'name_te': 'త్రికోణమితి అనువర్తనాలు', 'weightage': '6 - 8 Marks', 'questions': [{'id': 'D5-C12-Q1', 'marks': '1 Mark', 'q_en': 'Define angle of elevation and angle of depression.', 'q_te': 'ఊర్ధ్వ కోణం మరియు నిమ్న కోణం లను నిర్వచించండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'Line of Sight vs Horizontal'}, {'id': 'D5-C12-Q2', 'marks': '1 Mark', 'q_en': 'A tower stands vertically on ground. At point 15 m away from base, angle of elevation is 45°. Find tower height.', 'q_te': 'ఒక టవర్ అడుగు నుండి 15 మీ. దూరంలో ఉన్న బిందువు వద్ద ఊర్ధ్వ కోణం 45° అయితే టవర్ ఎత్తు ఎంత?', 'trend': 'TS 2024', 'concept': 'tan 45° = 1 => Height = Base = 15m'}, {'id': 'D5-C12-Q3', 'marks': '2 Marks', 'q_en': 'A kite is flying at height of 60 m above ground attached to string inclined at 60° to ground. Find string length.', 'q_te': 'ఒక గాలిపటం నేల నుండి 60 మీ. ఎత్తులో ఎగురుతూ, దారం నేలతో 60° కోణం చేస్తుంటే దారం పొడవు కనుగొనండి.', 'trend': 'AP 2023 (Ex 12.1 Q5)', 'concept': 'sin 60° = Opposite / Hypotenuse'}, {'id': 'D5-C12-Q4', 'marks': '2 Marks', 'q_en': 'The shadow of a tower is √3 times its height. Find the angle of elevation of the sun.', 'q_te': 'టవర్ నీడ పొడవు దాని ఎత్తుకు √3 రెట్లు ఉంటే సూర్యుని ఊర్ధ్వ కోణాన్ని కనుగొనండి.', 'trend': 'TS 2023', 'concept': 'tan θ = 1/√3 => θ = 30°'}, {'id': 'D5-C12-Q5', 'marks': '2 Marks', 'q_en': 'An observer 1.5 m tall is 28.5 m away from a chimney. Angle of elevation of top is 45°. Find height of chimney.', 'q_te': '1.5 మీ. ఎత్తు గల పరిశీలకుడు చిమ్నీ నుండి 28.5 మీ. దూరంలో ఉన్నాడు... చిమ్నీ ఎత్తు కనుగొనండి.', 'trend': 'AP 2024 (Ex 12.1 Q3)', 'concept': 'Adding Observer Height (28.5 + 1.5 = 30m)'}, {'id': 'D5-C12-Q6', 'marks': '4 Marks', 'q_en': 'A tree breaks due to storm and the broken part bends so that top of tree touches ground making an angle of 30°. Distance from foot of tree to point where top touches is 8 m. Find height of tree.', 'q_te': 'తుఫాను వల్ల ఒక చెట్టు విరిగి నేలను 30° కోణంతో తాకింది. చెట్టు అడుగు నుండి నేలను తాకిన బిందువుకు గల దూరం 8 మీ. అయితే అసలు చెట్టు ఎత్తు ఎంత?', 'trend': 'TS & AP Most Repeated (Ex 12.1 Q2)', 'concept': 'Tree Height = Broken Part (Hyp) + Standing (Opp)'}, {'id': 'D5-C12-Q7', 'marks': '4 Marks', 'q_en': 'A 1.2 m tall girl spots a balloon moving with wind at height of 88.2 m. Angle of elevation reduces from 60° to 30°. Find distance travelled by balloon.', 'q_te': '1.2 మీ. ఎత్తున్న బాలిక 88.2 మీ. ఎత్తులోని బెలూన్ ను చూసినప్పుడు ఊర్ధ్వ కోణం 60° నుండి 30° కు తగ్గింది... బెలూన్ ప్రయాణించిన దూరం ఎంత?', 'trend': 'AP 2023 (Ex 12.2 Q3)', 'concept': 'Two Angles of Elevation'}, {'id': 'D5-C12-Q8', 'marks': '4 Marks', 'q_en': 'From the top of a 7 m high building, angle of elevation of top of cable tower is 60° and angle of depression of foot is 45°. Determine height of tower.', 'q_te': '7 మీ. ఎత్తున్న భవనం పైనుండి కేబుల్ టవర్ పైభాగాన్ని చూస్తే ఊర్ధ్వ కోణం 60°, టవర్ అడుగును చూస్తే నిమ్న కోణం 45°... టవర్ ఎత్తు కనుగొనండి.', 'trend': 'TS 2024 (Ex 12.2 Q7)', 'concept': 'Elevation & Depression from Raised Point'}, {'id': 'D5-C12-Q9', 'marks': '8 Marks', 'q_en': 'Two poles of equal heights are standing opposite each other on either side of a road 80 m wide. From a point between them on road, angles of elevation of tops are 60° and 30°. Find height of poles and distance of point from poles.', 'q_te': '80 మీ. వెడల్పు గల రోడ్డుకు ఇరువైపులా సమాన ఎత్తు గల రెండు స్తంభాలున్నాయి. రోడ్డుపై ఒక బిందువు నుండి వాటి ఊర్ధ్వ కోణాలు 60°, 30° అయితే స్తంభాల ఎత్తు మరియు దూరాలను కనుగొనండి.', 'trend': 'TS & AP Guaranteed 8M (Ex 12.2 Q5)', 'concept': 'Equal Height Poles on Opposite Sides of Road'}, {'id': 'D5-C12-Q10', 'marks': '8 Marks', 'q_en': 'The angle of elevation of a cloud from a point 60 m above a lake is 30° and angle of depression of its reflection in the lake is 60°. Find the height of the cloud above the lake.', 'q_te': 'సరస్సు పైభాగం నుండి 60 మీ. ఎత్తులోని బిందువు నుండి మేఘం ఊర్ధ్వ కోణం 30°, దాని ప్రతిబింబం నిమ్న కోణం 60° అయితే సరస్సు ఉపరితలం నుండి మేఘం ఎత్తు కనుగొనండి.', 'trend': 'AP 2024, TS 2023 (Section IV 8M)', 'concept': 'Reflection in Water (Object Height = Image Depth)'}]}, {'id': 13, 'name_en': 'Probability', 'name_te': 'సంభావ్యత', 'weightage': '6 Marks', 'questions': [{'id': 'D5-C13-Q1', 'marks': '1 Mark', 'q_en': 'Define theoretical probability of an event E: P(E) = Number of outcomes favourable to E / Total number of possible outcomes.', 'q_te': 'ఒక ఘటన E యొక్క సంభావ్యత P(E) సూత్రాన్ని నిర్వచించండి.', 'trend': 'TS 2023, AP 2024', 'concept': 'P(E) = m / n'}, {'id': 'D5-C13-Q2', 'marks': '1 Mark', 'q_en': "If P(E) = 0.05, what is the probability of 'not E' (P(not E))?", 'q_te': "P(E) = 0.05 అయితే, 'E కాదు' యొక్క సంభావ్యత ఎంత?", 'trend': 'TS 2024 (Ex 13.1 Q5)', 'concept': "P(E') = 1 - P(E) = 0.95"}, {'id': 'D5-C13-Q3', 'marks': '2 Marks', 'q_en': 'A die is thrown once. Find the probability of getting: (i) a prime number (ii) a number lying between 2 and 6.', 'q_te': 'ఒక పాచికను ఒకసారి దొర్లించినప్పుడు (i) ప్రధాన సంఖ్య (ii) 2 మరియు 6 ల మధ్య సంఖ్య వచ్చే సంభావ్యత ఎంత?', 'trend': 'AP 2023 (Ex 13.1 Q13)', 'concept': 'Single Die 6 Outcomes'}, {'id': 'D5-C13-Q4', 'marks': '2 Marks', 'q_en': 'One card is drawn from a well-shuffled deck of 52 cards. Find probability of getting: (i) a king of red colour (ii) a face card.', 'q_te': 'బాగా కలిపిన 52 పేకముక్కల కట్ట నుండి ఒక కార్డు తీసినప్పుడు: (i) ఎరుపు రాజు (ii) చిత్ర కార్డు (Face card) వచ్చే సంభావ్యత ఎంత?', 'trend': 'TS 2023 (Ex 13.1 Q14)', 'concept': '52 Cards Probability Breakdown'}, {'id': 'D5-C13-Q5', 'marks': '2 Marks', 'q_en': 'A bag contains 3 red balls and 5 black balls. A ball is drawn at random. What is probability that ball is: (i) red (ii) not red?', 'q_te': 'ఒక సంచిలో 3 ఎరుపు, 5 నలుపు బంతులున్నాయి... తీసిన బంతి (i) ఎరుపు (ii) ఎరుపు కానిది కావడానికి సంభావ్యత ఎంత?', 'trend': 'AP 2024 (Ex 13.1 Q8)', 'concept': 'Balls in Bag Probability'}, {'id': 'D5-C13-Q6', 'marks': '4 Marks', 'q_en': 'Two dice are thrown at same time. What is probability that sum of two numbers appearing is: (i) 8 (ii) 13 (iii) less than or equal to 12?', 'q_te': 'రెండు పాచికలను ఒకేసారి దొర్లించినప్పుడు వాటిపై సంఖ్యల మొత్తం: (i) 8 (ii) 13 (iii) 12 లేదా అంతకంటే తక్కువ కావడానికి సంభావ్యత ఎంత?', 'trend': 'TS & AP Most Repeated (Ex 13.2 Q1)', 'concept': 'Two Dice 36 Outcomes Matrix'}, {'id': 'D5-C13-Q7', 'marks': '4 Marks', 'q_en': 'A box contains 90 discs numbered 1 to 90. If one disc is drawn at random, find probability that it bears: (i) a two-digit number (ii) a perfect square number (iii) a number divisible by 5.', 'q_te': '1 నుండి 90 వరకు సంఖ్యలు గల 90 బిళ్ళల నుండి ఒక బిళ్ళ తీస్తే: (i) రెండంకెల సంఖ్య (ii) ఖచ్చిత వర్గం (iii) 5 చే భాగించబడే సంఖ్య వచ్చే సంభావ్యత ఎంత?', 'trend': 'TS 2024 (Ex 13.1 Q18)', 'concept': 'Numbered Discs Selection'}, {'id': 'D5-C13-Q8', 'marks': '4 Marks', 'q_en': 'Five cards - ten, jack, queen, king and ace of diamonds are well-shuffled with face downwards. One card is drawn: (i) What is probability that card is queen? (ii) If queen is drawn and put aside, what is probability second card is: (a) ace (b) queen?', 'q_te': 'డైమండ్స్ లోని 10, జాకీ, రాణి, రాజు, ఏస్ లలో నుండి ఒక కార్డు తీస్తే రాణి వచ్చే సంభావ్యత ఎంత? రాణిని పక్కన పెడితే రెండవ కార్డు ఏస్ లేదా రాణి కావడానికి సంభావ్యత ఎంత?', 'trend': 'AP 2023 (Ex 13.1 Q15)', 'concept': 'Drawing Without Replacement'}, {'id': 'D5-C13-Q9', 'marks': '8 Marks', 'q_en': 'A carton consists of 100 shirts of which 88 are good, 8 have minor defects and 4 have major defects. Jimmy, a trader, will only accept shirts which are good. Sujatha, another trader, will only reject shirts which have major defects. One shirt is drawn at random. What is probability that: (i) it is acceptable to Jimmy? (ii) it is acceptable to Sujatha?', 'q_te': '100 చొక్కాలలో 88 మంచివి, 8 చిన్న లోపాలు, 4 పెద్ద లోపాలు గలవి... జిమ్మీ మంచివి మాత్రమే తీసుకుంటాడు, సుజాత పెద్ద లోపాలు గలవి తిరస్కరిస్తుంది... సంభావ్యతలు కనుగొనండి.', 'trend': 'TS 2024, AP 2024 (Ex 13.1 Q23 - 8M)', 'concept': 'Multi-conditional Probability Analysis'}, {'id': 'D5-C13-Q10', 'marks': '8 Marks', 'q_en': 'In a game, a coin is tossed 3 times and its result recorded each time. Hanif wins if all tosses give same result (i.e. 3 heads or 3 tails), and loses otherwise. (i) Write all possible outcomes. (ii) Calculate probability that Hanif will lose the game.', 'q_te': 'ఒక నాణేన్ని 3 సార్లు ఎగురవేసినప్పుడు: (i) సాధ్యమయ్యే అన్ని పర్యవసానాలను రాయండి. (ii) హనీఫ్ ఆటలో ఓడిపోయే సంభావ్యతను లెక్కించండి.', 'trend': 'AP 2023, TS 2023 (Ex 13.1 Q24)', 'concept': '3 Coins Tossing 8 Outcomes (HHH, HHT, ...)'}]}]}]
}

# =============================================================================
# 3. PREVIOUS SSC BOARD EXAM PAPERS (AP & TS)
# =============================================================================
PAST_PAPERS_DATA = [
    {
        "title": "TS SSC 2024 Mathematics Annual Board Examination",
        "year": "2024",
        "state": "Telangana (TS)",
        "exam_type": "Annual Public Examination (Single Paper - 80 Marks)",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Latest single-paper format examination consisting of Section I, II, III, and IV with internal choice in Section IV.",
        "download_url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
        "download_links": [
            {
                "label": "TS SSC 2024 Math Paper & Key (Sakshi Education)",
                "url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
                "type": "Paper & Answer Key"
            },
            {
                "label": "TS SSC Official BSE Portal",
                "url": "https://bse.telangana.gov.in/",
                "type": "Official Board Portal"
            }
        ]
    },
    {
        "title": "AP SSC 2024 Mathematics Annual Examination",
        "year": "2024",
        "state": "Andhra Pradesh (AP)",
        "exam_type": "Annual Public Examination (100 Marks)",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "AP SSC 2024 Board question paper with 33 questions across 4 sections.",
        "download_url": "https://www.eenadupratibha.net/ap-tenth/",
        "download_links": [
            {
                "label": "AP SSC 2024 Math Paper & Solutions (Eenadu Pratibha)",
                "url": "https://www.eenadupratibha.net/ap-tenth/",
                "type": "Paper & Solutions"
            },
            {
                "label": "AP SSC Official BSE Portal",
                "url": "https://bse.ap.gov.in/",
                "type": "Official Board Portal"
            }
        ]
    },
    {
        "title": "TS SSC 2023 Mathematics Annual Board Paper",
        "year": "2023",
        "state": "Telangana (TS)",
        "exam_type": "Annual Public Examination",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "TS SSC 2023 Board Examination Mathematics Question Paper with model answer key.",
        "download_url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
        "download_links": [
            {
                "label": "TS SSC 2023 Math Paper & Solutions",
                "url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
                "type": "Question Paper PDF"
            }
        ]
    },
    {
        "title": "AP SSC 2023 Mathematics Board Paper",
        "year": "2023",
        "state": "Andhra Pradesh (AP)",
        "exam_type": "Annual Public Examination",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "AP SSC 2023 Board Mathematics Question Paper.",
        "download_url": "https://www.eenadupratibha.net/ap-tenth/",
        "download_links": [
            {
                "label": "AP SSC 2023 Math Question Paper",
                "url": "https://www.eenadupratibha.net/ap-tenth/",
                "type": "Question Paper PDF"
            }
        ]
    },
    {
        "title": "TS & AP 2022 Mathematics Board Examination Papers",
        "year": "2022",
        "state": "Telangana & AP",
        "exam_type": "Board Examination Papers",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Post-pandemic streamlined question papers with increased internal choice.",
        "download_url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
        "download_links": [
            {
                "label": "TS & AP 2022 Math Board Papers",
                "url": "https://www.sakshieducation.com/ts-10th-class/question-papers",
                "type": "Archive"
            }
        ]
    },
    {
        "title": "Official SSC Mathematics Model Paper & Blueprint",
        "year": "Model Paper 2025",
        "state": "AP & TS State Boards",
        "exam_type": "Official Model Question Paper & Blueprint",
        "mediums": ["English Medium", "Telugu Medium"],
        "description": "Official SCERT blueprint demonstrating mark weightage by academic standards (Problem Solving: 40%, Reasoning & Proof: 20%, Communication: 10%, Connection: 15%, Representation & Visualization: 15%).",
        "download_url": "https://scert.telangana.gov.in/",
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
