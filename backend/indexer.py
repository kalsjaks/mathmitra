import os
import sys
import json
import re
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

EM_PDF = os.path.join("knowledgesource", "10 mathematics em 2023-24.pdf")
TM_PDF = os.path.join("knowledgesource", "X Mathematics TM 2026-27.pdf")
OUTPUT_INDEX = os.path.join("backend", "data", "textbook_index.json")

CHAPTER_METADATA = [
    {
        "id": 1,
        "name_en": "Real Numbers",
        "name_te": "వాస్తవ సంఖ్యలు",
        "start_page": 1,
        "end_page": 27,
        "pdf_page_start": 8,
        "pdf_page_end": 35,
        "exercises": ["1.1", "1.2", "1.3", "1.4", "1.5"],
        "key_formulas": [
            "a = bq + r \\quad (0 \\le r < b)",
            "\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b",
            "\\log_a (xy) = \\log_a x + \\log_a y",
            "\\log_a \\left(\\frac{x}{y}\\right) = \\log_a x - \\log_a y",
            "\\log_a (x^m) = m \\log_a x"
        ],
        "key_concepts_en": [
            "Euclid's Division Lemma: For positive integers a and b, there exist unique whole numbers q and r such that a = bq + r, where 0 <= r < b.",
            "Fundamental Theorem of Arithmetic: Every composite number can be expressed as a product of primes uniquely, apart from the order of factors.",
            "Revisiting Irrational Numbers: Proving that sqrt(2), sqrt(3), sqrt(5) are irrational using proof by contradiction.",
            "Terminating and Non-terminating Decimals: A rational number p/q has terminating decimal expansion if q = 2^n * 5^m.",
            "Logarithms and their laws."
        ],
        "key_concepts_te": [
            "యూక్లిడ్ భాగహార న్యాయం: a, b ధన పూర్ణ సంఖ్యలైతే, a = bq + r (0 <= r < b) అయ్యేటట్లు ఏకైక పూర్ణ సంఖ్యల జత q, r లు వ్యవస్థితమవుతాయి.",
            "అంకగణిత ప్రాథమిక సిద్ధాంతం: ప్రతి సంయుక్త సంఖ్యను ప్రధాన సంఖ్యల లబ్దంగా ఏకైకంగా రాయవచ్చు.",
            "కరణీయ సంఖ్యలు: రూట్ 2, రూట్ 3, రూట్ 5 మొదలైనవి కరణీయ సంఖ్యలని విరోధాభాస పద్ధతిలో నిరూపించడం.",
            "అంతమయ్యే మరియు అంతం కాని ఆవర్తన దశాంశాలు: హారం q = 2^n * 5^m రూపంలో ఉంటే ఆ దశాంశం అంతమవుతుంది.",
            "సంవర్గమానాలు మరియు వాటి నియమాలు."
        ]
    },
    {
        "id": 2,
        "name_en": "Sets",
        "name_te": "సమితులు",
        "start_page": 28,
        "end_page": 50,
        "pdf_page_start": 36,
        "pdf_page_end": 58,
        "exercises": ["2.1", "2.2", "2.3", "2.4"],
        "key_formulas": [
            "n(A \\cup B) = n(A) + n(B) - n(A \\cap B)",
            "A \\cup B = \\{x : x \\in A \\text{ or } x \\in B\\}",
            "A \\cap B = \\{x : x \\in A \\text{ and } x \\in B\\}",
            "A - B = \\{x : x \\in A \\text{ and } x \\notin B\\}"
        ],
        "key_concepts_en": [
            "Sets and Representation: Roster form and Set-builder form.",
            "Types of Sets: Empty set, Finite set, Infinite set, Universal set, Subset.",
            "Venn Diagrams and Operations: Union, Intersection, Difference of sets.",
            "Disjoint sets: A and B are disjoint if A \\cap B = \\emptyset."
        ],
        "key_concepts_te": [
            "సమితి భావన మరియు రూపాలు: రోస్టర్ రూపం మరియు సమితి నిర్మాణ రూపం.",
            "సమితుల రకాలు: శూన్య సమితి, పరిమిత సమితి, అపరిమిత సమితి, ఉపసమితి, విశ్వసమితి.",
            "వెన్ చిత్రాలు మరియు సమితి ప్రక్రియలు: సమ్మేళనం, ఛేదనం, సమితుల భేదం.",
            "వియుక్త సమితులు: A మరియు B ల ఛేదనం శూన్య సమితి అయితే (A ∩ B = Φ)."
        ]
    },
    {
        "id": 3,
        "name_en": "Polynomials",
        "name_te": "బహుపదులు",
        "start_page": 51,
        "end_page": 76,
        "pdf_page_start": 59,
        "pdf_page_end": 84,
        "exercises": ["3.1", "3.2", "3.3", "3.4"],
        "key_formulas": [
            "\\text{Linear: } p(x) = ax + b \\implies x = -\\frac{b}{a}",
            "\\text{Quadratic: } \\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha \\beta = \\frac{c}{a}",
            "p(x) = k[x^2 - (\\alpha + \\beta)x + \\alpha \\beta]",
            "\\text{Cubic: } \\alpha + \\beta + \\gamma = -\\frac{b}{a}, \\quad \\alpha \\beta + \\beta \\gamma + \\gamma \\alpha = \\frac{c}{a}, \\quad \\alpha \\beta \\gamma = -\\frac{d}{a}",
            "p(x) = g(x) \\cdot q(x) + r(x)"
        ],
        "key_concepts_en": [
            "Zeroes of a Polynomial: Values of x where p(x) = 0.",
            "Geometrical meaning: Number of points where graph crosses x-axis equals number of real zeroes.",
            "Relation between Zeroes and Coefficients for quadratic and cubic polynomials.",
            "Division Algorithm for Polynomials."
        ],
        "key_concepts_te": [
            "బహుపది శూన్యాలు: p(x) = 0 అయ్యే x విలువలు.",
            "జ్యామితీయ అర్థం: రేఖాచిత్రం X-అక్షాన్ని ఖండించే బిందువుల సంఖ్య శూన్యాల సంఖ్య అవుతుంది.",
            "శూన్యాలు మరియు గుణకాల మధ్య సంబంధం.",
            "బహుపదుల భాగహార న్యాయం."
        ]
    },
    {
        "id": 4,
        "name_en": "Pair of Linear Equations in Two Variables",
        "name_te": "రెండు చరరాశులలో రేఖీయ సమీకరణాల జత",
        "start_page": 77,
        "end_page": 104,
        "pdf_page_start": 85,
        "pdf_page_end": 112,
        "exercises": ["4.1", "4.2", "4.3"],
        "key_formulas": [
            "a_1 x + b_1 y + c_1 = 0, \\quad a_2 x + b_2 y + c_2 = 0",
            "\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2} \\implies \\text{Intersecting lines, Unique solution (Consistent)}",
            "\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} \\implies \\text{Coincident lines, Infinitely many solutions (Dependent)}",
            "\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2} \\implies \\text{Parallel lines, No solution (Inconsistent)}"
        ],
        "key_concepts_en": [
            "Methods of solving: Graphical method, Substitution method, Elimination method.",
            "Consistency and inconsistency conditions.",
            "Equations reducible to linear form."
        ],
        "key_concepts_te": [
            "సాధన పద్ధతులు: గ్రాఫ్ పద్ధతి, ప్రతిక్షేపణ పద్ధతి, చలరాశి తొలగింపు పద్ధతి.",
            "సంగత మరియు అసంగత సమీకరణాల నిబంధనలు.",
            "రేఖీయ సమీకరణాల రూపంలోకి మార్చగల సమీకరణాలు."
        ]
    },
    {
        "id": 5,
        "name_en": "Quadratic Equations",
        "name_te": "వర్గ సమీకరణాలు",
        "start_page": 105,
        "end_page": 128,
        "pdf_page_start": 113,
        "pdf_page_end": 136,
        "exercises": ["5.1", "5.2", "5.3", "5.4"],
        "key_formulas": [
            "ax^2 + bx + c = 0 \\quad (a \\ne 0)",
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
            "\\Delta = b^2 - 4ac",
            "\\Delta > 0 \\implies \\text{Two distinct real roots}",
            "\\Delta = 0 \\implies \\text{Two equal real roots}",
            "\\Delta < 0 \\implies \\text{No real roots}"
        ],
        "key_concepts_en": [
            "Standard form of Quadratic Equation.",
            "Solution by Factorisation method and Completing the Square method.",
            "Quadratic Formula (Sridharacharya Formula).",
            "Nature of roots using discriminant Delta."
        ],
        "key_concepts_te": [
            "వర్గ సమీకరణ ప్రామాణిక రూపం ax^2 + bx + c = 0.",
            "కారణాంక పద్ధతి మరియు వర్గాన్ని పూర్తి చేసే పద్ధతి ద్వారా సాధన.",
            "వర్గ సమీకరణ సూత్రం (శ్రీధరాచార్య సూత్రం).",
            "విచక్షణి (Delta) ఆధారంగా మూలాల స్వభావం."
        ]
    },
    {
        "id": 6,
        "name_en": "Progressions",
        "name_te": "శ్రేఢులు",
        "start_page": 129,
        "end_page": 162,
        "pdf_page_start": 137,
        "pdf_page_end": 170,
        "exercises": ["6.1", "6.2", "6.3", "6.4", "6.5"],
        "key_formulas": [
            "\\text{AP } n\\text{-th term: } a_n = a + (n-1)d",
            "\\text{AP Sum: } S_n = \\frac{n}{2}[2a + (n-1)d] = \\frac{n}{2}[a + l]",
            "\\text{GP } n\\text{-th term: } a_n = a r^{n-1}",
            "\\text{Common difference: } d = a_{n} - a_{n-1}",
            "\\text{Common ratio: } r = \\frac{a_{n}}{a_{n-1}}"
        ],
        "key_concepts_en": [
            "Arithmetic Progression (AP): Definition, first term a, common difference d.",
            "General term and sum of first n terms of an AP.",
            "Geometric Progression (GP): Definition, first term a, common ratio r, n-th term."
        ],
        "key_concepts_te": [
            "అంకశ్రేఢి (AP): మొదటి పదం a, సామాన్య భేదం d, n-వ పదం మరియు మొదటి n పదాల మొత్తం.",
            "గుణశ్రేఢి (GP): మొదటి పదం a, సామాన్య నిష్పత్తి r, n-వ పదం."
        ]
    },
    {
        "id": 7,
        "name_en": "Coordinate Geometry",
        "name_te": "నిరూపక రేఖాగణితం",
        "start_page": 163,
        "end_page": 194,
        "pdf_page_start": 171,
        "pdf_page_end": 202,
        "exercises": ["7.1", "7.2", "7.3", "7.4"],
        "key_formulas": [
            "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
            "P(x, y) = \\left(\\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}\\right)",
            "\\text{Midpoint} = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)",
            "\\text{Centroid } G = \\left(\\frac{x_1 + x_2 + x_3}{3}, \\frac{y_1 + y_2 + y_3}{3}\\right)",
            "\\text{Area} = \\frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|",
            "\\text{Slope } m = \\frac{y_2 - y_1}{x_2 - x_1} = \\tan \\theta"
        ],
        "key_concepts_en": [
            "Distance formula between two points.",
            "Section formula for internal division.",
            "Area of a triangle and condition for collinearity (Area = 0).",
            "Slope of a straight line."
        ],
        "key_concepts_te": [
            "రెండు బిందువుల మధ్య దూరం సూత్రం.",
            "విభజన సూత్రం (సెక్షన్ ఫార్ములా), మధ్య బిందువు, గురుత్వ కేంద్రం.",
            "త్రిభుజ వైశాల్యం మరియు సరేఖీయ బిందువుల నిబంధన (వైశాల్యం = 0).",
            "సరళరేఖ వాలు (Slope)."
        ]
    },
    {
        "id": 8,
        "name_en": "Similar Triangles",
        "name_te": "సరూప త్రిభుజాలు",
        "start_page": 195,
        "end_page": 228,
        "pdf_page_start": 203,
        "pdf_page_end": 236,
        "exercises": ["8.1", "8.2", "8.3", "8.4"],
        "key_formulas": [
            "\\text{BPT (Thales Theorem): } \\frac{AD}{DB} = \\frac{AE}{EC}",
            "\\frac{\\text{Area}(\\triangle ABC)}{\\text{Area}(\\triangle PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{AC}{PR}\\right)^2",
            "\\text{Pythagoras Theorem: } AC^2 = AB^2 + BC^2"
        ],
        "key_concepts_en": [
            "Basic Proportionality Theorem (Thales) and its converse.",
            "Criteria for similarity of triangles: AAA, SSS, SAS.",
            "Areas of similar triangles theorem.",
            "Pythagoras theorem and its converse."
        ],
        "key_concepts_te": [
            "ప్రాథమిక అనుపాత సిద్ధాంతం (థేల్స్ సిద్ధాంతం) మరియు దాని విపర్యయం.",
            "త్రిభుజాల సరూపతా నియమాలు: కో.కో.కో, భు.భు.భు, భు.కో.భు.",
            "సరూప త్రిభుజాల వైశాల్యాల సిద్ధాంతం.",
            "పైథాగరస్ సిద్ధాంతం మరియు దాని విపర్యయం."
        ]
    },
    {
        "id": 9,
        "name_en": "Tangents and Secants to a Circle",
        "name_te": "స్పర్శరేఖలు మరియు ఛేదనరేఖలు",
        "start_page": 229,
        "end_page": 248,
        "pdf_page_start": 237,
        "pdf_page_end": 256,
        "exercises": ["9.1", "9.2", "9.3"],
        "key_formulas": [
            "\\text{Length of tangents from external point: } PA = PB",
            "\\text{Area of Sector} = \\frac{x^\\circ}{360^\\circ} \\times \\pi r^2",
            "\\text{Length of arc } l = \\frac{x^\\circ}{360^\\circ} \\times 2 \\pi r",
            "\\text{Area of Segment} = \\text{Area of Sector} - \\text{Area of } \\triangle"
        ],
        "key_concepts_en": [
            "Tangent is perpendicular to the radius at the point of contact.",
            "Lengths of tangents drawn from an external point to a circle are equal.",
            "Area of sector and segment of a circle."
        ],
        "key_concepts_te": [
            "వృత్త స్పర్శబిందువు వద్ద గీసిన వ్యాసార్థం స్పర్శరేఖకు లంబంగా ఉంటుంది.",
            "బాహ్య బిందువు నుండి వృత్తానికి గీసిన స్పర్శరేఖల పొడవులు సమానం.",
            "సెక్టారు వైశాల్యం, చాపం పొడవు మరియు వృత్త ఖండ వైశాల్యం."
        ]
    },
    {
        "id": 10,
        "name_en": "Mensuration",
        "name_te": "క్షేత్రమితి",
        "start_page": 249,
        "end_page": 272,
        "pdf_page_start": 257,
        "pdf_page_end": 280,
        "exercises": ["10.1", "10.2", "10.3", "10.4"],
        "key_formulas": [
            "\\text{Cylinder: } CSA = 2\\pi r h, \\quad TSA = 2\\pi r(r + h), \\quad V = \\pi r^2 h",
            "\\text{Cone: } l = \\sqrt{r^2 + h^2}, \\quad CSA = \\pi r l, \\quad TSA = \\pi r(l + r), \\quad V = \\frac{1}{3}\\pi r^2 h",
            "\\text{Sphere: } SA = 4\\pi r^2, \\quad V = \\frac{4}{3}\\pi r^3",
            "\\text{Hemisphere: } CSA = 2\\pi r^2, \\quad TSA = 3\\pi r^2, \\quad V = \\frac{2}{3}\\pi r^3"
        ],
        "key_concepts_en": [
            "Surface area and volume of combination of solids (cone on cylinder, hemisphere on cylinder, etc.).",
            "Conversion of solid from one shape to another.",
            "Frustum of a cone concepts."
        ],
        "key_concepts_te": [
            "సంయుక్త ఘనపదార్థాల ఉపరితల వైశాల్యం మరియు ఘనపరిమాణం.",
            "ఒక ఆకారం నుండి మరొక ఆకారంలోకి ఘనపదార్థాల మార్పిడి."
        ]
    },
    {
        "id": 11,
        "name_en": "Trigonometry",
        "name_te": "త్రికోణమితి",
        "start_page": 273,
        "end_page": 297,
        "pdf_page_start": 281,
        "pdf_page_end": 305,
        "exercises": ["11.1", "11.2", "11.3", "11.4"],
        "key_formulas": [
            "\\sin \\theta = \\frac{opp}{hyp}, \\quad \\cos \\theta = \\frac{adj}{hyp}, \\quad \\tan \\theta = \\frac{opp}{adj}",
            "\\sin^2 \\theta + \\cos^2 \\theta = 1",
            "\\sec^2 \\theta - \\tan^2 \\theta = 1",
            "\\text{cosec}^2 \\theta - \\cot^2 \\theta = 1",
            "\\sin(90^\\circ - \\theta) = \\cos \\theta, \\quad \\tan(90^\\circ - \\theta) = \\cot \\theta, \\quad \\sec(90^\\circ - \\theta) = \\text{cosec } \\theta"
        ],
        "key_concepts_en": [
            "Trigonometric ratios in a right-angled triangle.",
            "Trigonometric ratios of specific angles: 0, 30, 45, 60, 90 degrees.",
            "Trigonometric ratios of complementary angles.",
            "Trigonometric Identities and their proofs."
        ],
        "key_concepts_te": [
            "లంబకోణ త్రిభుజంలో త్రికోణమితి నిష్పత్తులు.",
            "నిర్దిష్ట కోణాల (0, 30, 45, 60, 90 డిగ్రీలు) త్రికోణమితి విలువలు.",
            "పూరక కోణాల త్రికోణమితి నిష్పత్తులు.",
            "త్రికోణమితి సర్వసమీకరణాలు మరియు వాటి నిరూపణలు."
        ]
    },
    {
        "id": 12,
        "name_en": "Applications of Trigonometry",
        "name_te": "త్రికోణమితి అనువర్తనాలు",
        "start_page": 298,
        "end_page": 308,
        "pdf_page_start": 306,
        "pdf_page_end": 316,
        "exercises": ["12.1", "12.2"],
        "key_formulas": [
            "\\tan \\theta = \\frac{\\text{Height}}{\\text{Distance}}",
            "\\sin \\theta = \\frac{\\text{Opposite}}{\\text{Hypotenuse}}",
            "\\text{Angle of elevation: Observer looking up}",
            "\\text{Angle of depression: Observer looking down}"
        ],
        "key_concepts_en": [
            "Line of sight, horizontal line, angle of elevation, angle of depression.",
            "Calculating heights of towers, trees, buildings, and widths of rivers using trigonometry."
        ],
        "key_concepts_te": [
            "దృష్టి రేఖ, క్షితిజ సమాంతర రేఖ, ఊర్ధ్వ కోణం, నిమ్న కోణం.",
            "గోపురాలు, భవనాలు, వృక్షాల ఎత్తులు మరియు నదుల వెడల్పులను కనుగొనుట."
        ]
    },
    {
        "id": 13,
        "name_en": "Probability",
        "name_te": "సంభావ్యత",
        "start_page": 309,
        "end_page": 326,
        "pdf_page_start": 317,
        "pdf_page_end": 334,
        "exercises": ["13.1", "13.2"],
        "key_formulas": [
            "P(E) = \\frac{\\text{Number of outcomes favorable to } E}{\\text{Total number of possible outcomes}} = \\frac{n(E)}{n(S)}",
            "0 \\le P(E) \\le 1",
            "P(E) + P(\\bar{E}) = 1 \\implies P(\\bar{E}) = 1 - P(E)",
            "\\text{Sure event: } P = 1, \\quad \\text{Impossible event: } P = 0"
        ],
        "key_concepts_en": [
            "Random experiments, sample space, elementary events.",
            "Equally likely outcomes (coins, dice, cards).",
            "Complementary events, impossible events, certain events."
        ],
        "key_concepts_te": [
            "యాదృచ్ఛిక ప్రయోగాలు, పర్యవసానాలు, ఘటనలు.",
            "సమసంభవ పర్యవసానాలు (నాణాలు, పాచికలు, పేకముక్కలు).",
            "పూరక ఘటనలు, అసాధ్య ఘటన, ఖచ్చిత ఘటన."
        ]
    },
    {
        "id": 14,
        "name_en": "Statistics",
        "name_te": "సాంఖ్యక శాస్త్రం",
        "start_page": 327,
        "end_page": 356,
        "pdf_page_start": 335,
        "pdf_page_end": 364,
        "exercises": ["14.1", "14.2", "14.3", "14.4"],
        "key_formulas": [
            "\\text{Mean (Direct): } \\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}",
            "\\text{Mean (Assumed): } \\bar{x} = a + \\frac{\\sum f_i d_i}{\\sum f_i} \\quad (d_i = x_i - a)",
            "\\text{Mean (Step-Dev): } \\bar{x} = a + \\left(\\frac{\\sum f_i u_i}{\\sum f_i}\\right) \\cdot h \\quad (u_i = \\frac{x_i - a}{h})",
            "\\text{Mode} = l + \\left(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right) \\cdot h",
            "\\text{Median} = l + \\left(\\frac{\\frac{N}{2} - cf}{f}\\right) \\cdot h"
        ],
        "key_concepts_en": [
            "Mean of grouped data: Direct method, Assumed mean method, Step deviation method.",
            "Mode of grouped data using modal class.",
            "Median of grouped data using cumulative frequency (cf).",
            "Graphical representation of cumulative frequency distribution (Ogive curves)."
        ],
        "key_concepts_te": [
            "వర్గీకృత దత్తాంశపు సగటు: ప్రత్యక్ష పద్ధతి, ఊహించిన సగటు పద్ధతి, సోపాన విచలన పద్ధతి.",
            "వర్గీకృత దత్తాంశపు బాహుళకం సూత్రం.",
            "వర్గీకృత దత్తాంశపు మధ్యగతం సూత్రం మరియు సంచిత పౌనఃపున్యం.",
            "సంచిత పౌనఃపున్య వక్రాలు (ఓజీవ్ వక్రాలు)."
        ]
    }
]

def build_full_rag_index():
    print("Extracting detailed text chunks from English Medium textbook...")
    reader_em = pypdf.PdfReader(EM_PDF)
    
    extracted_exercises = {}
    page_texts = {}

    for idx, page in enumerate(reader_em.pages):
        page_num = idx + 1
        text = page.extract_text() or ""
        text_clean = re.sub(r'\s+', ' ', text).strip()
        page_texts[page_num] = text_clean

        # Check for Exercise headers
        ex_matches = re.finditer(r'Exercise\s*[-–]?\s*(\d+\.\d+)', text, re.IGNORECASE)
        for match in ex_matches:
            ex_num = match.group(1)
            # Find snippet around exercise
            start_pos = match.start()
            snippet = text[start_pos:start_pos+1500].strip()
            if ex_num not in extracted_exercises:
                extracted_exercises[ex_num] = {
                    "exercise": ex_num,
                    "pdf_page": page_num,
                    "snippet": snippet
                }

    print(f"Mapped {len(extracted_exercises)} exercises from PDF.")
    
    database = {
        "curriculum": "SSC Telangana & Andhra Pradesh 10th Mathematics",
        "total_chapters": len(CHAPTER_METADATA),
        "chapters": CHAPTER_METADATA,
        "exercises": extracted_exercises,
        "page_count": len(reader_em.pages)
    }

    os.makedirs(os.path.dirname(OUTPUT_INDEX), exist_ok=True)
    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully saved RAG database to {OUTPUT_INDEX}")

if __name__ == "__main__":
    build_full_rag_index()
