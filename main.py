import os
import random
import requests
from datetime import datetime

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# 1. 고화질 시각 인포그래픽 아카이브 (Visual Analysis)
ANALYSIS_ARCHIVE = [
    {
        "title": "🎬 [디렉터스 컷] 에스파(aespa) - 'Supernova'",
        "concept": "더치 틸트 25° 대각선 구도 & 네온 보색 충돌",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/supernova.png",
        "layout": "📐 **더치 틸트 & 1/3 분할 안착**: 카메라를 25° 기울여 정적인 누운 포즈에 강한 텐션을 부여하고, 얼굴과 시선은 좌하단 1/3 교차점에 정확히 고정.",
        "camera": "🎥 **스피드 램핑 & 스냅 줌**: 정박 안무 직전 슬로우로 프레임을 늘려 시각적 타격감 극대화.",
        "acting": "✨ **0.5초 시선 락온**: 나른하게 바닥을 보다가 턱을 살짝 들며 렌즈를 정면으로 꿰뚫는 마이크로 아이컨택.",
        "color": "🎨 **미드나잇 블루 vs 네온 마젠타**: 쿨톤 배경 속 단 하나의 마젠타 귀걸이(#FF007F)가 시각적 앵커 역할.",
        "director_tip": "💡 *Director's Note:* 인물이 가만히 누워있는 씬일수록 카메라 앵글을 비틀고(더치 틸트) 소품에 강렬한 보색 포인트를 주어야 텐션이 죽지 않습니다."
    },
    {
        "title": "🎬 [디렉터스 컷] 뉴진스(NewJeans) - 'Ditto'",
        "concept": "사이드 프로필 & Z축 3단 레이어링 구도",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/ditto.png",
        "layout": "📐 **Z축 깊이감 & 리드룸(Lead Room)**: 전경(해린)·중경(다니엘)·원경(민지)을 대각선 깊이감으로 배치하고 시선 방향 좌측을 2/3 비워두는 여백 연출.",
        "camera": "🎥 **핸드헬드 & 거친 패닝**: 인위적 트랙 대신 6mm 캠코더 특유의 미세한 손떨림으로 날것의 현장감 연출.",
        "acting": "✨ **엔딩 잔상 호흡**: 말을 건네지 않고 창밖을 묵묵히 응시하며 관찰자에게 아련한 거리감과 여운을 남기는 연기.",
        "color": "🎨 **교복 탄(#8A7B72) & 빈티지 그레이**: 인위적 네온을 배제하고 창가의 자연광과 필름 그레인으로 Y2K 감성 극대화.",
        "director_tip": "💡 *Director's Note:* 인물의 쓸쓸함이나 비밀스러운 무드를 살릴 땐 인물이 바라보는 방향의 리드룸을 과감하게 비워두세요."
    },
    {
        "title": "🎬 [디렉터스 컷] 아이브(IVE) - 'I AM'",
        "concept": "활주로 중심 1점 투시 & 완벽 대칭 구도",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/ive_iam.png",
        "layout": "📐 **수직 1점 대칭 원근**: 도로의 중앙선과 배경 스크린을 정중앙 축으로 삼고 양옆에 대칭으로 멤버를 배치해 신화적 위압감 형성.",
        "camera": "🎥 **익스트림 하이앵글 & 드론 풀아웃**: 지상에서 상공으로 수직 비상하는 카메라 무빙으로 카타르시스 전달.",
        "acting": "✨ **냉미녀 갭 모에 스머크**: 날카로운 무표정을 유지하다가 후렴구 진입 순간 입꼬리 한쪽만 피식 올리는 여유.",
        "color": "🎨 **런웨이 나이트 & 조명 기둥 시안**: 딥 네이비 배경에 뻗어나가는 차가운 조명 빔으로 맑고 세련된 스케일감 완성.",
        "director_tip": "💡 *Director's Note:* 다인원 그룹의 당당함을 표현할 때는 바닥의 소실점과 상공 조명의 방사형 라인을 일치시키는 1점 대칭 구도가 가장 강력합니다."
    },
    {
        "title": "🎬 [디렉터스 컷] 방탄소년단(BTS) - '피 땀 눈물'",
        "concept": "최후의 만찬 사선 원근 & 야수파 유화 미학",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/bts_bst.png",
        "layout": "📐 **사선 하이앵글 테이블 구도**: 만찬 테이블을 대각선으로 틀어 호스트(진)에게 시선이 자연스럽게 모이도록 유도.",
        "camera": "🎥 **스테디캠 글라이딩 & 슬로우 트래킹**: 박물관 복도를 미끄러지듯 유영하는 무빙으로 몽환적 탐미주의 극대화.",
        "acting": "✨ **손끝 마이크로 제스처**: 와인잔을 쥔 손가락 관절의 섬세한 긴장감과 목선으로 이어지는 절제된 유혹 연기.",
        "color": "🎨 **야수파 마젠타 스카이 vs 순백 수트**: 불타는 듯한 비현실적 유화 배경과 성스러운 올 화이트 수트의 강렬한 충돌.",
        "director_tip": "💡 *Director's Note:* 클래식 회화 모티브의 씬에서는 인물의 동선을 최소화하고 조명과 배경의 색채 대비로 드라마틱한 무게감을 잡아야 합니다."
    },
    {
        "title": "🎬 [디렉터스 컷] 르세라핌(LE SSERAFIM) - 'EASY'",
        "concept": "고딕 성당 & 90s 네온 그런지 발코니 구도",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/lesserafim_easy.png",
        "layout": "📐 **발코니 극단적 로우 앵글**: 아래에서 멤버들을 올려다보는 앙각 구도로 5명의 당당한 애티튜드(Attitude)를 영웅적으로 부각.",
        "camera": "🎥 **비트 줌 펄스(Zoom Pulse)**: 90년대 올드스쿨 붐뱁 그루브에 맞춰 카메라가 미세하게 바운스를 타며 튕겨나가는 연출.",
        "acting": "✨ **시선 락온 & 턱짓 액팅**: 정면 카메라를 아래로 내려다보며 살짝 고개를 젖히는 특유의 당당한 제스처.",
        "color": "🎨 **바이올렛 림라이트 & 키치 네온**: 고딕 성당의 장엄한 보라색 역광 속에 불타는 하트와 눈동자 네온사인을 파격 배치.",
        "director_tip": "💡 *Director's Note:* 힙합 그루브 기반의 군무는 카메라가 정적인 삼각대 위에 머물지 않고 댄서의 스텝과 호흡을 같이 타야 진짜 맛이 납니다."
    }
]

# 2. 데일리 연출 스터디 퀴즈 아카이브 (Daily Director Quiz)
QUIZ_ARCHIVE = [
    {
        "question": "Q1. 인물이 누워있거나 정적인 씬에서 심리적 불안감이나 강렬한 긴장감을 부여하기 위해 수평선을 20~30도 비틀어 촬영하는 앵글 기법은?",
        "options": "1️⃣ 버드 아이즈 뷰 (Bird's Eye View)\n2️⃣ 더치 틸트 (Dutch Tilt / Canted Angle)\n3️⃣ 오비탈 샷 (Orbital Tracking Shot)\n4️⃣ 웜즈 아이 뷰 (Worm's Eye View)",
        "answer": "2번 더치 틸트 (Dutch Tilt)",
        "explanation": "수평을 의도적으로 깨뜨려 관객의 뇌에 시각적 불안과 에너지를 전달하는 고전적이면서도 가장 강력한 연출 기법입니다. (예: 에스파 'Supernova' 윈터 도입부)",
        "scene_ref": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/supernova.png"
    },
    {
        "question": "Q2. 비트가 터지는 킬링파트 직전에 프레임을 120fps 슬로우로 늘렸다가 순간적으로 24fps 원배속으로 낚아채며 시각적 타격감을 주는 편집 기법은?",
        "options": "1️⃣ 점프 컷 (Jump Cut)\n2️⃣ 크로스 디졸브 (Cross Dissolve)\n3️⃣ 스피드 램핑 (Speed Ramping)\n4️⃣ 매치 컷 (Match Cut)",
        "answer": "3번 스피드 램핑 (Speed Ramping)",
        "explanation": "시간의 흐름을 왜곡시켜 관객의 호흡을 쥐락펴락하는 기법으로, K-POP 댄스 브레이크와 임팩트 모션의 90% 이상에 쓰입니다.",
        "scene_ref": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/ive_iam.png"
    },
    {
        "question": "Q3. 피사체 뒤편에서 강한 역광을 쏘아 인물의 외곽선 실루엣을 빛나게 만들어 어두운 배경과 피사체를 3D처럼 명확히 분리해 주는 조명 기법은?",
        "options": "1️⃣ 림 라이트 (Rim / Edge Light)\n2️⃣ 키 라이트 (Key Light)\n3️⃣ 플랫 라이트 (Flat Light)\n4️⃣ 바운스 라이트 (Bounce Light)",
        "answer": "1번 림 라이트 (Rim Light)",
        "explanation": "사이버펑크, 성당, 지하 클럽 등 어두운 톤의 뮤비 씬에서 인물의 윤곽을 살리고 몽환적인 후광 효과를 줄 때 필수적으로 사용하는 세팅입니다.",
        "scene_ref": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/lesserafim_easy.png"
    },
    {
        "question": "Q4. 전혀 다른 두 씬 사이를 전환할 때, 형태나 움직임이 유사한 오브젝트(원형 바퀴 ➡️ 찻잔, 턴 동작 ➡️ 회전문)를 이어붙여 시각적 연속성을 만드는 트랜지션은?",
        "options": "1️⃣ 페이드 아웃 (Fade Out)\n2️⃣ 매치 컷 (Match Cut / Graphic Match)\n3️⃣ 윕 팬 (Whip Pan)\n4️⃣ L-컷 (L-Cut)",
        "answer": "2번 매치 컷 (Match Cut)",
        "explanation": "단순한 컷 전환을 넘어 시공간을 초월하는 세련된 은유를 완성할 때 디렉터들이 가장 애용하는 시각적 속임수 기법입니다.",
        "scene_ref": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/bts_bst.png"
    }
]

def send_mv_analysis():
    if not WEBHOOK_URL:
        print("❌ DISCORD_WEBHOOK_URL 환경 변수가 설정되지 않았습니다.")
        return

    today = datetime.now().strftime("%Y년 %m월 %d일")
    mode = random.choice(["analysis", "quiz"])

    if mode == "analysis":
        item = random.choice(ANALYSIS_ARCHIVE)
        embed = {
            "title": item["title"],
            "description": f"**핵심 콘셉트:** {item['concept']}\n*30년 차 디렉터의 실전 연출 & 레이아웃 시각 인포그래픽*",
            "color": 0x00E5FF,
            "image": {"url": item["image_url"]},
            "fields": [
                {"name": "📐 구도 및 레이아웃 분할", "value": item["layout"], "inline": False},
                {"name": "🎥 카메라 무빙 & 트랜지션", "value": item["camera"], "inline": False},
                {"name": "✨ 덕심 저격 마이크로 액팅", "value": item["acting"], "inline": False},
                {"name": "🎨 컬러 그레이딩 & 조명", "value": item["color"], "inline": False},
                {"name": "💡 디렉터의 실무 노트", "value": item["director_tip"], "inline": False}
            ],
            "footer": {"text": f"Pickle MV Director Visual Archive • {today}"}
        }
        msg = "오늘의 시각 연출 아카이브가 도착했습니다! 🎬"
    else:
        quiz = random.choice(QUIZ_ARCHIVE)
        embed = {
            "title": "🧠 [디렉터스 퀴즈] 오늘의 실전 연출 감각 트레이닝",
            "description": f"**{quiz['question']}**\n\n{quiz['options']}\n\n━━━━━━━━━━━━━━━━━━━━\n👇 **정답 & 디렉터 해설 확인 (클릭)**\n||**정답:** {quiz['answer']}\n**해설:** {quiz['explanation']}||",
            "color": 0xFFD700,
            "image": {"url": quiz["scene_ref"]},
            "footer": {"text": f"Pickle Director Training Quiz • {today}"}
        }
        msg = "오늘의 연출 퀴즈가 도착했습니다! 스포일러를 누르기 전에 답을 먼저 맞춰보세요. 🎯"

    payload = {
        "username": "MV 디렉터 스터디 룸",
        "avatar_url": "https://images.unsplash.com/photo-1518173946687-a4c8a383392e?w=128&auto=format&fit=crop&q=80",
        "content": msg,
        "embeds": [embed]
    }

    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code == 204:
        print(f"✅ 디스코드로 전송 완료! (모드: {mode})")
    else:
        print(f"⚠️ 전송 실패: {resp.status_code} - {resp.text}")

# ==========================================
# 3. 앨범 아트 & 패키징 비주얼 아카이브 연동
# ==========================================
from album_art import send_album_art_analysis

# main 실행 시 기존 MV 분석과 앨범아트 채널 발송을 함께 수행
_original_main = send_mv_analysis

def run_all_archives():
    print("🚀 [1/2] MV 연출 & 퀴즈 아카이브 발송 중...")
    _original_main()
    print("🚀 [2/2] 앨범 아트 & 비주얼 디자인 아카이브 발송 중...")
    try:
        send_album_art_analysis()
    except Exception as e:
        print(f"⚠️ 앨범아트 발송 실패: {e}")

if __name__ == "__main__":
    run_all_archives()
