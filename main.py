import os
import random
import requests
from datetime import datetime

# 디스코드 웹훅 URL (GitHub Actions Secrets에서 주입)
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# 30년 차 뮤비 디렉터의 아이돌 MV 연출 & 레이아웃 분석 아카이브 (고화질 스틸컷 포함)
ANALYSIS_ARCHIVE = [
    {
        "title": "🎬 [씬 바이 씬] 에스파(aespa) - 'Supernova'",
        "concept": "SF 미장센 & 키치 글리치 / 초능력 연출",
        "image_url": "https://i.ytimg.com/vi/phuiiNCxRMg/maxresdefault.jpg",
        "layout": "📐 **광각 로우앵글 & 중심 소실점 구도**: 인물을 화면 정중앙에 배치하고 배경을 왜곡시켜 비현실적인 히어로의 강렬한 위압감을 극대화했습니다.",
        "camera": "🎥 **스피드 램핑(Speed Ramping)**: 빠른 안무 컷 직전에 슬로우 모션을 걸어 타격감과 시각적 임팩트를 강하게 부여합니다.",
        "color": "🎨 **사이버 네온 & 하이 콘트라스트**: 차가운 블루 톤 베이스에 강렬한 마젠타/그린 보색 대비를 입혀 미래지향적 사이버펑크 톤을 완성했습니다.",
        "director_tip": "💡 *Director's Note:* 초현실적인 CG 연출일수록 세트의 물리적 텍스처(아스팔트 균열, 금속 광택)를 리얼하게 살려야 유치함을 피할 수 있습니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 뉴진스(NewJeans) - 'Ditto'",
        "concept": "Y2K 아날로그 질감 & 노스탤지어",
        "image_url": "https://i.ytimg.com/vi/pSUydWEqKwE/maxresdefault.jpg",
        "layout": "📐 **4:3 화면비 & 프레임 인 프레임**: 6mm 캠코더 뷰파인더 구도를 활용해 '관찰자(반희수)'의 시선으로 아련한 거리감과 몰입감을 형성합니다.",
        "camera": "🎥 **핸드헬드 & 거친 패닝**: 인위적인 트래킹 대신 손떨림을 그대로 살려 마치 실제 학창 시절 홈비디오 같은 날것의 현장감을 연출했습니다.",
        "color": "🎨 **로우 채도 & 웜 그레이 톤**: 채도를 낮추고 필름 그레인(노이즈)을 입혀 오래 바랜 필름 사진 같은 질감을 살렸습니다.",
        "director_tip": "💡 *Director's Note:* 클로즈업 샷에서 인물을 중앙보다 화면 한쪽 모서리에 치우치게 배치하면 특유의 결핍과 아련한 그리움이 살아납니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 아이브(IVE) - 'I AM'",
        "concept": "하이패션 시네마틱 & 압도적 스케일",
        "image_url": "https://i.ytimg.com/vi/6ZUIwj3FgUY/maxresdefault.jpg",
        "layout": "📐 **광활한 오픈 프레임 & 대칭 구도**: 비행기 활주로와 구름 위 배경을 시원하게 개방하여 당당한 해방감과 스케일감을 부여했습니다.",
        "camera": "🎥 **익스트림 하이앵글 & 드론 줌아웃**: 높은 곳에서 지상으로 수직 낙하하거나 상공으로 솟구치는 무빙으로 비상하는 카타르시스를 전달합니다.",
        "color": "🎨 **클린 화이트 & 딥 블루**: 군더더기 없는 화이트와 하늘의 딥 블루를 메인 컬러로 잡아 세련되고 맑은 고급스러움을 연출했습니다.",
        "director_tip": "💡 *Director's Note:* 점프하는 씬에서 공중에 머무는 '체공 시간'을 슬로우로 살짝 늘려주면 모션의 우아함과 드라마가 극대화됩니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 방탄소년단(BTS) - '피 땀 눈물'",
        "concept": "고전 회화 미학 & 유혹의 알레고리",
        "image_url": "https://i.ytimg.com/vi/hmE9f-TEutc/maxresdefault.jpg",
        "layout": "📐 **완벽한 좌우 대칭(Symmetry)**: 바티칸 건축물과 명화를 연상시키는 기하학적 대칭 구조로 신화적이고 웅장한 무게감을 구축했습니다.",
        "camera": "🎥 **스테디캠 글라이딩 샷**: 박물관 복도를 유영하듯 부드럽게 미끄러지는 카메라 워크로 몽환적인 탐미주의를 강조했습니다.",
        "color": "🎨 **바로크풍 벨벳 & 골드 섀도우**: 어두운 섀도우 속에 반사되는 금빛 오브제와 비비드한 원색의 감각적인 조화가 특징입니다.",
        "director_tip": "💡 *Director's Note:* 미술적 상징이 많은 세트에서는 인물 뒤에 림라이트(배경 윤곽광)를 세밀하게 분리해야 피사체의 입체감이 묻히지 않습니다."
    },
    {
        "title": "🎬 [씬 바이 씬] 르세라핌(LE SSERAFIM) - 'EASY'",
        "concept": "90s 올드스쿨 힙합 & 그런지 시네마",
        "image_url": "https://i.ytimg.com/vi/bNKXxwOQYB8/maxresdefault.jpg",
        "layout": "📐 **2.35:1 시네마스코프 레터박스**: 가로로 긴 영화 화면비를 채택하여 묵직하고 클래식한 필름 영화의 룩을 재현했습니다.",
        "camera": "🎥 **로우 앵글 스텝 트래킹**: 발목 높이에서 댄서들의 바운스를 따라가는 로우 앵글로 힙합 그루브의 묵직함을 극대화했습니다.",
        "color": "🎨 **성당 스테인드글라스 & 네온 그런지**: 장엄한 성당 내부에 파격적인 네온사인과 그린 틴트를 충돌시켜 반항적인 무드를 연출했습니다.",
        "director_tip": "💡 *Director's Note:* 그루브 중심의 군무는 카메라가 댄서의 비트에 맞춰 살짝 줌 펄스(Zoom Pulse)를 튕겨줄 때 리듬감이 배가됩니다."
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
        "image": {
            "url": item["image_url"]
        },
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
        print("✅ 디스코드로 스크린샷 포함 분석 자료 전송 완료!")
    else:
        print(f"⚠️ 전송 실패: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    send_mv_analysis()
