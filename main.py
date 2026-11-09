import os
import random
import requests
from datetime import datetime

# 디스코드 웹훅 URL (GitHub Actions Secrets에서 주입)
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# 30년 차 뮤비 디렉터의 아이돌 MV 연출 & 레이아웃 분석 아카이브
ANALYSIS_ARCHIVE = [
    {
        "title": "🎬 [씬 바이 씬] 에스파(aespa) - 'Supernova'",
        "concept": "SF 미장센 & 키치 글리치 / 초능력 연출",
        "layout": "📐 **광각 로우앵글 & 중심 소실점 구도**: 인물을 화면 중앙에 두고 배경을 왜곡시켜 초현실적인 히어로 무드를 극대화함.",
        "camera": "🎥 **스피드 램핑(Speed Ramping)**: 빠른 안무 파트 직전 슬로우 모션을 걸어 타격감과 시각적 임팩트를 부여.",
        "color": "🎨 **사이버틱 네온 & 하이 콘트라스트**: 차가운 블루 톤 베이스에 강렬한 마젠타/그린 보색 대비로 미래지향적 톤 완성.",
        "director_tip": "💡 *Director's Note:* 초능력이나 비현실적 콘셉트일수록 세트의 텍스처(아스팔트 균열, 금속 광택)를 리얼하게 살려야 유치함을 피할 수 있습니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 뉴진스(NewJeans) - 'Ditto'",
        "concept": "Y2K 아날로그 질감 & 노스탤지어",
        "layout": "📐 **4:3 화면비 & 프레임 인 프레임**: 6mm 캠코더 뷰파인더 구도를 활용해 '관찰자(반희수)'의 시선으로 아련한 거리감 형성.",
        "camera": "🎥 **핸드헬드 & 거친 패닝**: 인위적인 트래킹 대신 손떨림을 살려 다큐멘터리 같은 자연스러운 현장감 연출.",
        "color": "🎨 **로우 채도 & 웜 그레이 톤**: 채도를 낮추고 그레인(노이즈)을 더해 바랜 필름 사진 같은 질감 표현.",
        "director_tip": "💡 *Director's Note:* 인물의 얼굴을 클로즈업할 때 화면 가장자리에 여백을 두면 특유의 쓸쓸함과 그리움이 배가됩니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 아이브(IVE) - 'I AM'",
        "concept": "하이패션 시네마틱 & 압도적 해방감",
        "layout": "📐 **광활한 오픈 프레임 & 대칭 구도**: 비행기 활주로와 구름 위 배경을 넓게 개방해 당당함과 스케일감 부여.",
        "camera": "🎥 **익스트림 하이앵글 & 드론 줌아웃**: 높은 곳에서 아래로 떨어지거나 위로 솟구치는 무빙으로 비상하는 카타르시스 전달.",
        "color": "🎨 **클린 화이트 & 딥 블루**: 군더더기 없는 화이트와 하늘의 딥 블루를 메인 컬러로 잡아 고급스러운 무드 완성.",
        "director_tip": "💡 *Director's Note:* 점프하는 순간 공중에 머무는 '체공 시간'을 슬로우로 살짝 늘려주면 모션의 우아함이 극대화됩니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 방탄소년단(BTS) - '피 땀 눈물'",
        "concept": "고전 회화 미학 & 유혹의 알레고리",
        "layout": "📐 **완벽한 좌우 대칭(Symmetry)**: 바티칸 건축물과 명화를 연상시키는 기하학적 대칭 구조로 신화적 무게감 형성.",
        "camera": "🎥 **스테디캠 트래킹 샷**: 박물관 복도를 유영하듯 부드럽게 미끄러지는 카메라 워크로 몽환적인 탐미주의 강조.",
        "color": "🎨 **바로크풍 벨벳 & 골드 쉐도우**: 어두운 섀도우 속에 반사되는 금빛 오브제와 비비드한 원색의 감각적 조화.",
        "director_tip": "💡 *Director's Note:* 예술적 상징이 많은 뮤비는 인물 뒤의 배경 조명(림라이트)을 세밀하게 분리해 피사체의 입체감을 살려야 합니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 르세라핌(LE SSERAFIM) - 'EASY'",
        "concept": "90s 올드스쿨 힙합 & 그런지 시네마",
        "layout": "📐 **2.35:1 시네마스코프 레터박스**: 가로로 긴 와이드 화면비를 채택해 영화 필름 같은 묵직함 부여.",
        "camera": "🎥 **로우 앵글 스텝 트래킹**: 발목 높이에서 댄서들의 바운스를 따라가는 로우 앵글로 힙합 그루브 극대화.",
        "color": "🎨 **성당 스테인드글라스 & 네온 그런지**: 차분한 성당 내부에 파격적인 네온사인과 그린 틴트를 입혀 반항적인 무드 연출.",
        "director_tip": "💡 *Director's Note:* 그루브 중심의 안무는 카메라가 댄서의 박자에 맞춰 살짝 줌 펄스(Zoom Pulse)를 줄 때 비트감이 살아납니다."
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
        "description": f"**콘셉트:** {item['concept']}\n*30년 차 디렉터의 데일리 아이돌 뮤비 연출 아카이빙*",
        "color": 0x8A2BE2,  # 세련된 퍼플 톤
        "fields": [
            {"name": "레이아웃 & 구도", "value": item["layout"], "inline": False},
            {"name": "카메라 무빙 & 트랜지션", "value": item["camera"], "inline": False},
            {"name": "색감 & 조명 미장센", "value": item["color"], "inline": False},
            {"name": "디렉터의 실무 팁", "value": item["director_tip"], "inline": False}
        ],
        "footer": {
            "text": f"Pickle MV Director Archive • {today}"
        }
    }

    payload = {
        "username": "MV 디렉터 아카이브",
        "avatar_url": "https://images.unsplash.com/photo-1518173946687-a4c8a383392e?w=128&auto=format&fit=crop&q=80",
        "embeds": [embed]
    }

    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code == 204:
        print("✅ 디스코드로 분석 자료 전송 완료!")
    else:
        print(f"⚠️ 전송 실패: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    send_mv_analysis()
