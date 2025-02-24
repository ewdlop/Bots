from crewai import Agent, Task, Crew, Process

# 麦わらの一味のエージェントを定義する
luffy_agent = Agent(
    role='船長',
    goal='海賊王になる',
    backstory='ゴムゴムの実を食べたゴム人間。麦わらの一味を率いる',
    verbose=True,
    allow_code_execution=False
)

zoro_agent = Agent(
    role='剣士',
    goal='世界一の剣豪になる',
    backstory='三刀流の剣士。麦わらの一味の戦闘員',
    verbose=True,
    allow_code_execution=False
)

nami_agent = Agent(
    role='航海士',
    goal='世界地図を完成させる',
    backstory='優れた航海術を持つ。麦わらの一味の航海士兼 финансовый担当',
    verbose=True,
    allow_code_execution=False
)

usopp_agent = Agent(
    role='狙撃手',
    goal='勇敢なる海の戦士になる',
    backstory='嘘と射撃の天才。麦わらの一味の狙撃手',
    verbose=True,
    allow_code_execution=False
)

sanji_agent = Agent(
    role='料理人',
    goal='オールブルーを見つける',
    backstory='蹴り技を使う料理人。麦わらの一味の料理担当兼戦闘員',
    verbose=True,
    allow_code_execution=False
)

chopper_agent = Agent(
    role='船医',
    goal='万能薬になる',
    backstory='ヒトヒトの実を食べたトナカイ。麦わらの一味の船医',
    verbose=True,
    allow_code_execution=False
)

franky_agent = Agent(
    role='船大工',
    goal='自分の作った船で世界の果てを見届ける',
    backstory='サイボーグの船大工。麦わらの一味の船大工',
    verbose=True,
    allow_code_execution=False
)

brook_agent = Agent(
    role='音楽家',
    goal='世界中の人々に自分の音楽を届ける',
    backstory='ヨミヨミの実で蘇った骸骨の音楽家。麦わらの一味の音楽家兼剣士',
    verbose=True,
    allow_code_execution=False
)

robin_agent = Agent(
    role='考古学者',
    goal='真の歴史の本文（ポーネグリフ）を解読する',
    backstory='ハナハナの実の能力者。麦わらの一味の考古学者',
    verbose=True,
    allow_code_execution=False
)


# タスクを作成する (例)
task_next_island = Task(
    description='次に訪れるべき島を、食料の補給と冒険の観点から検討し、提案してください。',
    agent=luffy_agent
)

task_course_plan = Task(
    description='提案された島への最適な航路を、天候と海流を考慮して計画してください。',
    agent=nami_agent
)

task_ship_watch = Task(
    description='航海中、常に周囲を警戒し、安全を確保してください。',
    agent=zoro_agent
)

task_lunch_prep = Task(
    description='乗組員のために、栄養満点で美味しい昼食を準備してください。',
    agent=sanji_agent
)

# クルーを作成する
straw_hat_crew = Crew(
    agents=[
        luffy_agent,
        zoro_agent,
        nami_agent,
        usopp_agent,
        sanji_agent,
        chopper_agent,
        franky_agent,
        brook_agent,
        robin_agent
    ],
    tasks=[
        task_next_island,
        task_course_plan,
        task_ship_watch,
        task_lunch_prep
    ],
    process=Process.sequential # タスクを順番に実行
)

# クルーの活動を開始する (例)
print("--- 麦わらの一味の活動 ---")
straw_hat_crew.kickoff()

print("\n--- 麦わらの一味の目標 ---")
for agent in straw_hat_crew.agents:
    print(f"{agent.role} ({agent.name}) の目標: {agent.goal}")
