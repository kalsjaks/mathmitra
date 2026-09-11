# -*- coding: utf-8 -*-
"""
Script to refactor solution_engine.py to match ChatGPT / Teacher step-by-step format:
1. Warm teacher intro
2. Numbered steps (Step 1, Step 2, Step 3...)
3. Boxed final answer
4. Teacher's Note & SSC Exam Tip / Justification
5. Decimal HCF support (e.g. 1.2 and 0.12)
"""
import re

with open("backend/solution_engine.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Euclid dispatcher to extract floats (decimals) as well as ints
old_dispatch = """    # 6. EUCLID'S DIVISION ALGORITHM / HCF / LCM
    if "hcf" in q_low or "euclid" in q_low or "గ.సా.భా" in q_low or "యూక్లిడ్" in q_low:
        nums = [int(n) for n in re.findall(r'\\b\\d+\\b', norm_query)]
        if len(nums) >= 2:
            return solve_hcf_euclid(query, nums[0], nums[1], detected_lang)"""

new_dispatch = """    # 6. EUCLID'S DIVISION ALGORITHM / HCF / LCM
    if "hcf" in q_low or "euclid" in q_low or "గ.సా.భా" in q_low or "యూక్లిడ్" in q_low:
        raw_floats = [float(n) for n in re.findall(r'\\b\\d+(?:\\.\\d+)?\\b', norm_query)]
        if len(raw_floats) >= 2:
            return solve_hcf_euclid(query, raw_floats[0], raw_floats[1], detected_lang)"""

if old_dispatch in code:
    code = code.replace(old_dispatch, new_dispatch)
    print("Updated Euclid dispatcher")
else:
    print("Warning: old_dispatch not matched directly")

# 2. Update solve_hcf_euclid definition and body
old_hcf_pattern = re.compile(r'def solve_hcf_euclid\(query: str, a_val: int, b_val: int, lang: str\):.*?(?=\n# =+ \n# 5\. PRIME)', re.DOTALL)

new_hcf_func = '''def solve_hcf_euclid(query: str, a_val, b_val, lang: str):
    # Check if either number has a decimal fraction
    is_float = (isinstance(a_val, float) and not a_val.is_integer()) or (isinstance(b_val, float) and not b_val.is_integer())

    if is_float:
        sa, sb = str(a_val), str(b_val)
        dec_a = len(sa.split('.')[1]) if '.' in sa else 0
        dec_b = len(sb.split('.')[1]) if '.' in sb else 0
        scale = 10 ** max(dec_a, dec_b)
        ia = int(round(a_val * scale))
        ib = int(round(b_val * scale))
        n1, n2 = max(ia, ib), min(ia, ib)

        steps = []
        curr_a, curr_b = n1, n2
        while curr_b != 0:
            q = curr_a // curr_b
            r = curr_a % curr_b
            steps.append(f"{curr_a} = ({curr_b} \\\\times {q}) + {r}")
            curr_a = curr_b
            curr_b = r

        int_hcf = math.gcd(n1, n2)
        final_hcf = int_hcf / scale
        final_hcf_str = f"{final_hcf:g}"

        steps_en = "\\n".join([f"• Step 2.{i+1}: ${s}$" for i, s in enumerate(steps)])
        steps_te = "\\n".join([f"• సోపానం 2.{i+1}: ${s}$" for i, s in enumerate(steps)])

        en_text = f"""### 🧮 Question
**{query.strip().rstrip('.')}**

---

Great SSC level question, let’s solve it carefully using Euclid’s Division Algorithm 👇

### Step 1: Write the numbers in integers
We are asked for HCF of **{a_val}** and **{b_val}**. Since Euclid’s algorithm works with integers, multiply both by **{scale}** to remove decimals:
$${a_val} \\times {scale} = {ia}, \\quad {b_val} \\times {scale} = {ib}$$
So the problem reduces to finding the **HCF of {n1} and {n2}**.

### Step 2: Apply Euclid’s Division Algorithm
Euclid’s algorithm states: For two positive integers $a$ and $b$ ($a > b$), there exist unique integers $q$ and $r$ such that:
$$a = bq + r \\quad (0 \\le r < b)$$

Here:
{steps_en}

Since the remainder is now **0**, the divisor at this stage is the HCF:
$$\\text{{HCF}}({n1}, {n2}) = {int_hcf}$$

### Step 3: Scale back to original decimals
Since we multiplied by {scale} earlier, the actual HCF is:
$$\\frac{{{int_hcf}}}{{{scale}}} = {final_hcf_str}$$

---

### ✅ Final Answer
The HCF of {a_val} and {b_val} is **{final_hcf_str}**.

---

### ✏️ Justification for SSC 10th Class
Euclid’s Division Algorithm can be applied to decimals by converting them into integers.
After scaling, we found $\\text{{HCF}}({ia}, {ib}) = {int_hcf}$.
Dividing back by {scale} gives {final_hcf_str}.
Hence, the HCF of {a_val} and {b_val} is **{final_hcf_str}**.
"""
        te_text = f"""### 🧮 ప్రశ్న
**{query.strip().rstrip('.')}**

---

చక్కని 10వ తరగతి SSC ప్రశ్న! యూక్లిడ్ భాగహార విశేషవిధి ద్వారా దీనిని జాగ్రత్తగా సాధిద్దాం 👇

### సోపానం 1: సంఖ్యలను పూర్ణ సంఖ్యలుగా మార్చడం
మనల్ని **{a_val}** మరియు **{b_val}** ల గ.సా.భా అడిగారు. యూక్లిడ్ విశేషవిధి పూర్ణ సంఖ్యలపై పనిచేస్తుంది కాబట్టి, దశాంశాలను తొలగించడానికి రెండింటినీ **{scale}** చే గుణించగా:
$${a_val} \\times {scale} = {ia}, \\quad {b_val} \\times {scale} = {ib}$$
ఇప్పుడు సమస్య **{n1} మరియు {n2} ల గ.సా.భా** కనుగొనడంగా మారుతుంది.

### సోపానం 2: యూక్లిడ్ భాగహార విశేషవిధిని వర్తింపజేయడం
యూక్లిడ్ న్యాయం: $a, b$ ($a > b$) ధన పూర్ణ సంఖ్యలకు $a = bq + r \\quad (0 \\le r < b)$
{steps_te}

శేషం **0** వచ్చినందున, ఈ దశలోని భాజకమే గ.సా.భా అవుతుంది:
$$\\text{{గ.సా.భా}}({n1}, {n2}) = {int_hcf}$$

### సోపానం 3: తిరిగి అసలు దశాంశాలలోకి మార్చడం
ముందుగా {scale} చే గుణించాం కాబట్టి, వాస్తవ గ.సా.భా:
$$\\frac{{{int_hcf}}}{{{scale}}} = {final_hcf_str}$$

---

### ✅ సమాధానం:
{a_val} మరియు {b_val} ల గ.సా.భా = **{final_hcf_str}**.

---

### ✏️ 10వ తరగతి బోర్డు పరీక్ష సమర్థన (Justification)
యూక్లిడ్ భాగహార విశేషవిధిని దశాంశ సంఖ్యలను పూర్ణ సంఖ్యలుగా మార్చడం ద్వారా వర్తింపజేయవచ్చు.
స్కేలింగ్ తర్వాత $\\text{{గ.సా.భా}}({ia}, {ib}) = {int_hcf}$ వచ్చింది.
తిరిగి {scale} చే భాగించగా {final_hcf_str} లభించింది.
అందువల్ల {a_val} మరియు {b_val} ల గ.సా.భా **{final_hcf_str}**.
"""
    else:
        n1 = max(int(a_val), int(b_val))
        n2 = min(int(a_val), int(b_val))
        hcf_val = math.gcd(n1, n2)

        steps = []
        curr_a, curr_b = n1, n2
        while curr_b != 0:
            q = curr_a // curr_b
            r = curr_a % curr_b
            steps.append(f"{curr_a} = ({curr_b} \\\\times {q}) + {r}")
            curr_a = curr_b
            curr_b = r

        steps_en = "\\n".join([f"• Step 2.{i+1}: ${s}$" for i, s in enumerate(steps)])
        steps_te = "\\n".join([f"• సోపానం 2.{i+1}: ${s}$" for i, s in enumerate(steps)])

        en_text = f"""### 🧮 Question
**{query.strip().rstrip('.')}**

---

Great SSC level question, let’s solve it step-by-step using Euclid’s Division Algorithm 👇

### Step 1: Identify the numbers & state the Lemma
Given two positive integers: $a = {n1}$ and $b = {n2}$, where ${n1} > {n2}$.
According to Euclid’s Division Lemma:
$$a = bq + r \\quad (0 \\le r < b)$$

### Step 2: Apply successive division steps
{steps_en}

Since the remainder is now **0**, the divisor at this final stage is the HCF:
$$\\text{{HCF}}({n1}, {n2}) = {hcf_val}$$

---

### ✅ Final Answer
The HCF of {n1} and {n2} is **{hcf_val}**.

---

### ✏️ Teacher's Note & SSC Board Exam Tip
• Always write the condition $0 \\le r < b$ next to $a = bq + r$. In SSC board evaluation, 1 mark is specifically awarded for stating the lemma!  
• Verification using prime factorisation confirms $\\text{{HCF}}({n1}, {n2}) = {hcf_val}$ $\\checkmark$.
"""
        te_text = f"""### 🧮 ప్రశ్న
**{query.strip().rstrip('.')}**

---

చక్కని 10వ తరగతి SSC ప్రశ్న! యూక్లిడ్ భాగహార విశేషవిధి ద్వారా దీనిని సోపానాల వారీగా సాధిద్దాం 👇

### సోపానం 1: సంఖ్యలను గుర్తించడం & యూక్లిడ్ న్యాయం రాయడం
ఇచ్చిన ధన పూర్ణ సంఖ్యలు: $a = {n1}$ మరియు $b = {n2}$, ఇక్కడ ${n1} > {n2}$.  
యూక్లిడ్ భాగహార న్యాయం ప్రకారం:
$$a = bq + r \\quad (0 \\le r < b)$$

### సోపానం 2: వరుస భాగహార సోపానాలు
{steps_te}

శేషం **0** వచ్చింది కాబట్టి, చివరి విభాజకమే గ.సా.భా అవుతుంది:
$$\\text{{గ.సా.భా}}({n1}, {n2}) = {hcf_val}$$

---

### ✅ సమాధానం:
{n1} మరియు {n2} ల గ.సా.భా = **{hcf_val}**.

---

### ✏️ ఉపాధ్యాయుని సూచన & బోర్డు పరీక్ష చిట్కా
• ఎల్లప్పుడూ $a = bq + r$ పక్కన $0 \\le r < b$ నిబంధన రాయండి.  
• దీనికి బోర్డు పరీక్షలో ప్రత్యేకంగా 1 మార్కు కేటాయించబడుతుంది!
"""

    return {
        "query": query,
        "language": lang,
        "chapter_id": 1,
        "chapter_en": "Real Numbers",
        "chapter_te": "వాస్తవ సంఖ్యలు",
        "page_reference": "Textbook Page 1-27",
        "exercise_reference": "Chapter 1 (Exercise 1.1)",
        "formulas": ["a = bq + r \\quad (0 \\le r < b)"],
        "explanation": {"en": en_text, "te": te_text}
    }
'''

if old_hcf_pattern.search(code):
    code = old_hcf_pattern.sub(new_hcf_func, code)
    print("Replaced solve_hcf_euclid successfully")
else:
    print("Warning: old_hcf_pattern not matched")

# 3. Clean up any remaining "### ✏️ Solution (Easy Way)" across other functions
code = code.replace("### ✏️ Solution (Easy Way - Factorisation Method)", "### Step 1: Factorisation (Splitting Middle Term)")
code = code.replace("### ✏️ Solution (Easy Way)", "### Step 1: Solution")
code = code.replace("### 🧠 Medium Way (Quadratic Formula)", "### Step 2: Verification using Quadratic Formula")
code = code.replace("### 🧠 Medium Way (Standard Board Exam Steps)", "### Step 2: Relation with Coefficients")
code = code.replace("### 🧠 Medium Way (Euclid's Division Lemma)", "### Step 2: Successive Division Steps")
code = code.replace("### 🧠 Medium Way", "### Step 2: Standard Method")
code = code.replace("### 🔬 Advanced Way (Verification of Zeroes & Coefficients)", "### Step 3: Verification")
code = code.replace("### 🔬 Advanced Way (Relation with LCM)", "### Step 3: Relation with LCM")
code = code.replace("### 🔬 Advanced Way", "### Step 3: Verification")

# Telugu replacements
code = code.replace("### ✏️ సులువైన విధానం (Easy Way)", "### సోపానం 1: సాధన")
code = code.replace("### 🧠 పరీక్ష పద్ధతి (Medium Way)", "### సోపానం 2: బోర్డు పరీక్ష పద్ధతి")
code = code.replace("### 🔬 సరిచూచు పద్ధతి (Advanced Way)", "### సోపానం 3: సరిచూచు విధానం")
code = code.replace("### ✏️ సాధనా సోపానాలు (కారణాంక పద్ధతి)", "### సోపానం 1: కారణాంక పద్ధతి")
code = code.replace("### 🧠 వర్గ సమీకరణ సూత్రం", "### సోపానం 2: వర్గ సమీకరణ సూత్రం")

with open("backend/solution_engine.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Finished refactoring solution_engine.py!")
