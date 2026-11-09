import os
import random
import requests
from datetime import datetime

# 디스코드 웹훅 URL (GitHub Actions Secrets에서 주입)
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# 30년 차 뮤비 디렉터의 아이돌 MV 연출 & 레이아웃 시각 인포그래픽 아카이브
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

def send_mv_analysis():
    if not WEBHOOK_URL:
        print("❌ DISCORD_WEBHOOK_URL 환경 변수가 설정되지 않았습니다.")
        return

    item = random.choice(ANALYSIS_ARCHIVE)
    today = datetime.now().strftime("%Y년 %m월 %d일")

    embed = {
        "title": item["title"],
        "description": f"**핵심 콘셉트:** {item['concept']}\n*30년 차 디렉터의 실전 연출 & 레이아웃 시각 인포그래픽*",
        "color": 0x00E5FF,  # 시안 네온 톤
        "image": {
            "url": item["image_url"]
        },
        "fields": [
            {"name": "📐 구도 및 레이아웃 분할", "value": item["layout"], "inline": False},
            {"name": "🎥 카메라 무빙 & 트랜지션", "value": item["camera"], "inline": False},
            {"name": "✨ 덕심 저격 마이크로 액팅", "value": item["acting"], "inline": False},
            {"name": "🎨 컬러 그레이딩 & 조명", "value": item["color"], "inline": False},
            {"name": "💡 디렉터의 실무 노트", "value": item["director_tip"], "inline": False}
        ],
        "footer": {
            "text": f"Pickle MV Director Visual Archive • {today}"
        }
    }

    payload = {
        "username": "MV 디렉터 아카이브",
        "avatar_url": "https://images.unsplash.com/photo-1518173946687-a4c8a383392e?w=128&auto=format&fit=crop&q=80",
        "embeds": [embed]
    }

    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code == 204:
        print("✅ 디스코드로 시각 인포그래픽 분석 자료 전송 완료!")
    else:
        print(f"⚠️ 전송 실패: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    send_mv_analysis()
