CHAT_WITH_BOT_TEMPLATE = (
    "You are an AI chatbot interacting with a user. Your goal is to provide helpful, relevant, and thoughtful responses to current user's input. Be informative and engaging.\n\n"
)

USER_INTENTION_CLASSIFY_TEMPLATE = (
    """ 
    You are an AI assistant that classifies user inputs into predefined categories. The categories and their descriptions are as follows:

    1. **Work_Recommendation**: When the user asks for recommendations on small tasks (suited to their condition or preferences).
    2. **Credit_Inquiry**: When the user requests to check the balance of "Yeopjeon" (credits or points).
    3. **General_Conversation**: When the input does not fit into the above categories.

    Classify the user's input into one of these categories. Respond with the category name only.

### Examples: 
    **Category: Work_Recommendation**
    User Input: "내 소일거리 추천해줘"
    Output: "Work_Recommendation"

    User Input: "일거리 추천해줘"
    Output: "Work_Recommendation"

    User Input: "다리가 아픈데 일거리 추천해줘"
    Output: "Work_Recommendation"

    User Input: "사무직 관련 일거리 추천해줘"
    Output: "Work_Recommendation"

    **Category: Credit_Inquiry**
    User Input: "엽전 남은 금액 조회해줘"
    Output: "Credit_Inquiry"

    User Input: "남은 엽전 조회해줘"
    Output: "Credit_Inquiry"

    User Input: "남은 엽전 얼마야?"
    Output: "Credit_Inquiry"

    User Input: "남은 엽전 크레딧 조회"
    Output: "Credit_Inquiry"

    User Input: "엽전 크레딧 조회"
    Output: "Credit_Inquiry"

    **Category: General_Conversation**
    User Input: "안녕?"
    Output: "General_Conversation"

    User Input: "안녕하세요"
    Output: "General_Conversation"

    User Input: "오늘 심심해"
    Output: "General_Conversation"

    User Input: "오늘 날씨 어때?"
    Output: "General_Conversation"
    """
)


ENTITY_EXTRACTION_PROMPT = (
    """
    You are an AI assistant that extracts specific entities from user input. Please analyze the input text and extract the following four entities:

    ### Entities
    1. Location (위치)
       Extract any location information mentioned in the text.
       - Use the exact location if mentioned (e.g., "서울시 강남구", "도봉구", "시흥시 은행동", "경북 구미", "대전광역시 유성구", "경기도 부천시")
       - Use "UNKNOWN" if no location is mentioned

    2. Physical Condition (신체 상태)
       - NORMAL: Person has no physical limitations and can exercise normally
       - FRAIL: Person has difficulty with physical movement
       - PRE_FRAIL: Person can move but has limitations with active physical activities
       - UNKNOWN: If it doesn't fall into any of the categories above

    3. Previous Occupation Category (현재, 과거 직종)
       Extract the person's current or previous occupation and classify into one of:
       - ACCOUNTING_FINANCE: 회계, 재무 관련 업무
       - ARCADE_PC_ROOM: 오락실, PC방 관련 업무
       - AUTO_REPAIR_SHIPBUILDING: 자동차 수리, 조선 관련 업무
       - BEAUTY: 미용 관련 업무
       - BUS_TAXI_VAN: 버스, 택시, 밴 운전 업무
       - CARGO_SPECIAL_VEHICLES: 화물, 특수차량 운전 업무
       - CAR_WASH_REFUELING: 세차, 주유 관련 업무
       - CHAUFFEUR: 운전기사 업무
       - CHEF_COOK: 주방장, 요리사 업무
       - CLEANING_SANITATION: 청소, 위생 관련 업무
       - CLOTHING_ACCESSORIES: 의류, 악세서리 판매 업무
       - CONSTRUCTION_FINISHING: 건설 마감 업무
       - CONSTRUCTION_SITE: 건설 현장 업무
       - CONSTRUCTION_STRUCTURE: 건설 구조물 업무
       - CONVENIENCE_STORE: 편의점 관련 업무
       - COSMETICS_BEAUTY: 화장품, 미용 판매 업무
       - COUNTER: 카운터 업무
       - DAYCARE: 보육 관련 업무
       - DELIVERY_MOVING: 배달, 이사 업무
       - DEPARTMENT_STORE: 백화점 관련 업무
       - DOCTOR: 의사 업무
       - ELDERLY_CARE: 노인 돌봄 업무
       - ELECTRICAL_MANAGEMENT: 전기 관리 업무
       - ENTRANCE_EXAM: 입시 관련 업무
       - FARM_AGRICULTURE: 농장, 농업 관련 업무
       - FINANCE_INSURANCE: 금융, 보험 업무
       - FLORIST: 꽃집 관련 업무
       - FOOD_MANUFACTURING: 식품 제조 업무
       - FUNERAL_WEDDING: 장례식장, 웨딩홀 업무
       - GENERAL_AFFAIRS: 총무 업무
       - GENERAL_SALES: 일반 영업 업무
       - GOLF: 골프장 관련 업무
       - HIGHWAY_REST_STOP: 고속도로 휴게소 업무
       - HOTEL_LODGING: 호텔, 숙박 관련 업무
       - HOUSEKEEPER_BABYSITTER: 가사도우미, 베이비시터 업무
       - INBOUND_CS: 인바운드 고객상담 업무
       - INDEPENDENT_CONTRACTOR: 독립 계약자 업무
       - INSTALLATION_REPAIR: 설치, 수리 업무
       - IT_DESIGN: IT, 디자인 관련 업무
       - KITCHEN_STAFF: 주방 보조 업무
       - LARGE_RETAIL_STORE: 대형 소매점 업무
       - LAUNDRY_ALTERATION: 세탁, 수선 업무
       - LIVESTOCK_PRODUCE: 축산물, 농산물 관련 업무
       - MACHINERY_EQUIPMENT: 기계, 장비 관련 업무
       - MART_SUPERMARKET: 마트, 수퍼마켓 업무
       - MEDICAL_TECHNICIAN: 의료 기사 업무
       - METALWORK_MOLD: 금속가공, 금형 업무
       - MUSIC_ART: 음악, 예술 관련 업무
       - NURSING_ASSISTANT: 간호조무사 업무
       - OFFICE_PLANNING: 사무, 기획 업무
       - OTHER_CONSTRUCTION: 기타 건설 관련 업무
       - OTHER_COOKING_SERVING: 기타 요리, 서빙 업무
       - OTHER_DRIVING_DELIVERY: 기타 운전, 배달 업무
       - OTHER_EDUCATION: 기타 교육 관련 업무
       - OTHER_LIFESTYLE: 기타 생활 서비스 업무
       - OTHER_MEDICAL_CARE: 기타 의료, 간호 업무
       - OTHER_OFFICE_WORK: 기타 사무직 업무
       - OTHER_PRODUCTION_TECHNICAL: 기타 생산, 기술 업무
       - OTHER_SALES_CONSULTING: 기타 영업, 상담 업무
       - OTHER_SALES_DISTRIBUTION: 기타 판매, 유통 업무
       - OTHER_SERVICE: 기타 서비스 업무
       - OUTBOUND_TM: 아웃바운드 텔레마케팅 업무
       - PACKAGING_INSPECTION: 포장, 검사 업무
       - PARCEL_DELIVERY: 택배 배달 업무
       - PARKING_MANAGEMENT: 주차 관리 업무
       - PET_SHOP: 반려동물 관련 업무
       - PLUMBING_FACILITIES: 배관, 설비 업무
       - PRIVATE_TUTORING: 개인 교습 업무
       - PRODUCTION_MANUFACTURING: 생산, 제조 업무
       - QUICK_SERVICE: 퀵서비스 업무
       - REAL_ESTATE: 부동산 관련 업무
       - RECEPTION_SECRETARY: 리셉션, 비서 업무
       - SAUNA_SPA: 사우나, 스파 업무
       - SECURITY_GUARD: 경비, 보안 업무
       - SERVING_PACKAGING: 서빙, 포장 업무
       - SPORTS: 스포츠 관련 업무
       - SPORTS_INSTRUCTION: 스포츠 강습 업무
       - STORE_MANAGER: 매장 관리자 업무
       - STUDY_CAFE: 스터디카페 관련 업무
       - TEXTILE: 섬유 관련 업무
       - WELDING_CUTTING: 용접, 절단 업무
       - UNKNOWN: If it doesn't fall into any of the categories above

    4. Preferred Occupation Category (선호 직종)
       Classify preferred occupation using the same categories as above.

    ### Output Format
    Return string as "{location}, {physical_condition}, {experience}, {preference}"
    (e.g. "서울시 강남구, NORMAL, ACCOUNTING_FINANCE, SPORTS_INSTRUCTION")
    - Elements should be separated by ', ' (comma followed by a space)
    - Use "UNKNOWN" for any undetermined entity
    - Make sure there are no single or double quotes in the output

    ### Examples
    User Input: "저는 강남구에서 회계사로 일하다가 은퇴했는데, 아직 건강해서 운동도 잘하고 있어요. 이제는 체육관에서 운동 가르치는 일을 하고 싶네요."
    Output: 서울시 강남구, NORMAL, ACCOUNTING_FINANCE, SPORTS_INSTRUCTION

    User Input: "도봉구에서 공장 생산직으로 일했었는데, 요즘은 몸이 많이 약해져서 걷기도 힘들어요. 앞으로는 가벼운 편의점 알바를 찾고 있습니다."
    Output: 도봉구, FRAIL, PRODUCTION_MANUFACTURING, CONVENIENCE_STORE

    User Input: "시흥시에서 택시기사였는데, 요즘은 오래 운전하면 좀 힘들어요. 편의점에서 가벼운 일을 찾고 있습니다."
    Output: 시흥시, PRE_FRAIL, BUS_TAXI_VAN, CONVENIENCE_STORE

    User Input: "경비 일하고 있는데 다른 일 알아보고 싶어요."
    Output: UNKNOWN, UNKNOWN, SECURITY_GUARD, UNKNOWN

    User Input: "내 근처의 주차 관리직 찾아줘"
    Output: UNKNOWN, UNKNOWN, UNKNOWN, PARKING_MANAGEMENT

    User Input: "경북 구미에서 공장 일하다가 은퇴했어요. 이제는 편한 일을 찾고 있습니다."
    Output: 경북 구미, PRE_FRAIL, PRODUCTION_MANUFACTURING, UNKNOWN

    User Input: "대전광역시 유성구에서 할 수 있는 일자리 있나요?"
    Output: 대전광역시 유성구, UNKNOWN, UNKNOWN, UNKNOWN

    User Input: "경기도 부천시에서 간호조무사로 일했는데, 이제는 좀 더 편한 일을 찾고 있어요."
    Output: 경기도 부천시, UNKNOWN, NURSING_ASSISTANT, UNKNOWN
    """
)


