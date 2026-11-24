import streamlit as st

# 1. 리스트(list) 선언 (snake_case 준수)
formulas = ["HCl", "H2SO4", "H2O", "NaOH", "KOH", "Ca(OH)2"]
names = ["염산", "황산", "증류수(물)", "수산화나트륨", "수산화칼륨", "수산화칼슘"]
acid_list = ["HCl", "H2SO4"]

# 2. 함수(def) & 선택구조(if-elif-else)
def check_substance(formula):
    if formula in acid_list:
        return "산성입니다"
    elif formula == "H2O":
        return "중성입니다"
    else:
        return "염기성입니다"

# 3. Streamlit 웹 화면 구성
st.title("🧪 화학식 기반 산성·염기성 물질 판독기")

selected = st.radio("판독할 화학식을 클릭하세요:", formulas, horizontal=True)

result = check_substance(selected)
idx = formulas.index(selected)

st.metric(label=f"선택한 화학식: {selected} ({names[idx]})", value=result)

# 4. 반복구조(for)로 전체 분류표 출력
table_data = []
for i in range(len(formulas)):
    table_data.append({
        "화학식": formulas[i],
        "물질명": names[i],
        "판독 결과": check_substance(formulas[i])
    })
st.table(table_data)
