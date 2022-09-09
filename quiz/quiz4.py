def std_weight(height, gender):
    kg = 0
    m_height = height / 100
    if gender == "M" or gender == "m":
        kg = round(m_height ** 2 * 22, 2)  # 소수 둘째자리까지 나타내는 모습이다
        print(f"키 {height}cm 남자의 표준 체중은 {kg}kg 입니다.")
    elif gender == "F" or gender == "f":
        kg = round(m_height ** 2 * 21, 2)
        print(f"키 {height}cm 여자의 표준 체중은 {kg}kg 입니다.")


std_weight(160, "f")
