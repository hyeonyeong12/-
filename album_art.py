import os
import random
import requests
from datetime import datetime

# 앨범아트 채널 웹훅 URL (환경 변수 또는 기본 웹훅)
WEBHOOK_URL = os.environ.get(
    "DISCORD_ALBUM_ART_WEBHOOK_URL",
    "https://discord.com/api/webhooks/1569374950358257674/CEgmox_JFXo2BunGErIyU91yp-anVpLZwV3urNSWu4YrbAEQ0UTuDE08AdGtuK8kcGYv"
)

ALBUM_ART_ARCHIVE = [
    {
        "title": "🎨 [아트 디렉터스 컷] 에스파(aespa) - 'Armageddon'",
        "concept": "3D 크롬 메탈릭 타이포그래피 & CDP 피지컬 패키징 미학",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/supernova.png",
        "color": 0xFF007F,
        "typography": "• **3D 리퀴드 크롬(Liquid Chrome)**: 차가운 금속성과 외계 생명체의 유기적 곡선을 결합한 독보적 심볼릭 로고타입.\n• **네오 고딕 세리프**: 종말론적 세계관을 뒷받침하는 날카로운 가시 형태의 획 마감.",
        "packaging": "• **실제 구동 CDP(CD 플레이어) 한정판**: 스트리밍 시대에 피지컬 음반의 본질인 '음악을 듣는 행위'를 오브제화하여 소장 가치 극대화.\n• **투명 클리어 바디 & 사이버 그런지 그래픽**: 내부 회로 기판이 비치는 90s 테크노 무드와 Y2K 퓨처리즘의 완벽한 융합.",
        "texture": "• **하이 콘트라스트 실버 & 네온 마젠타**: 칠흑 같은 딥 블랙 배경 위에 극단적으로 반사되는 금속 광택 하이라이트.\n• **에칭 인쇄 & 메탈릭 헤어라인**: 슬리브 후가공에 거친 금속 헤어라인 질감 구현.",
        "director_note": "💡 *\"앨범 아트는 음악의 시각적 얼굴입니다. 곡의 세계관이 SF/사이버펑크라면 폰트의 반사광 하나까지 곡의 베이스 사운드 질감과 일치시켜야 합니다.\""
    },
    {
        "title": "🎨 [아트 디렉터스 컷] 뉴진스(NewJeans) - 'Get Up'",
        "concept": "Y2K 픽셀 아트와 '비치백(Beach Bag)' 피지컬 패키징",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/ditto.png",
        "color": 0x33CCFF,
        "typography": "• **레트로 픽셀 비트맵 폰트**: 2000년대 초반 아케이드 게임기와 초기 웹 감성을 환기하는 볼드한 픽셀 타이포.\n• **파워퍼프걸 협업 캐릭터 심볼**: 각 멤버의 시각적 개성을 2D 레트로 애니메이션 스타일로 완벽하게 치환.",
        "packaging": "• **실제 착용 가능한 '비치백(Bag)' 패키징**: 종이 박스 앨범의 고정관념을 깨고, 실생활에서 들고 다닐 수 있는 가방 자체가 앨범이 되는 패션 아이템화.\n• **토이(Toy) 패키징 미학**: 장난감 블리스터 패키지를 연상시키는 투명 PVC 재질로 키치한 여름 무드 극대화.",
        "texture": "• **파스텔 네온 & 비비드 원색 팔레트**: 시안 블루, 버블검 핑크, 레몬 옐로우의 경쾌한 Y2K 색채.\n• **매트 코팅 스티커 & 포토카드북**: 소장하고 꾸미는 재미(다꾸 문화)를 피지컬 음반에 완벽히 이식.",
        "director_note": "💡 *\"피지컬 앨범을 책장에 꽂아두는 '문서'가 아니라, 손에 쥐고 거리를 나설 수 있는 '패션 오브제'로 전환시키는 것이 현대 앨범 디자인의 핵심입니다.\""
    },
    {
        "title": "🎨 [아트 디렉터스 컷] f(x) - 'Pink Tape'",
        "concept": "K-POP 아트 디렉팅의 전설: VHS 비디오테이프 실물 패키징",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/lesserafim_easy.png",
        "color": 0xE0218A,
        "typography": "• **핸드라이팅 & 빈티지 라벨러 폰트**: 마치 개인이 직접 비디오테이프 라벨 스티커에 타자기로 찍어낸 듯한 아날로그 타이포.\n• **레트로 로맨티시즘 레이아웃**: 규칙적인 그리드를 일부러 무너뜨린 스크랩북 스타일 타이포그래피.",
        "packaging": "• **완벽한 VHS 비디오테이프 형태**: 플라스틱 케이스의 규격부터 테이프 릴의 디테일, 라벨 스티커의 배치까지 90년대 비디오테이프를 정교하게 복각.\n• **아트필름 스틸컷 포토북**: 뮤비 촬영 현장의 35mm 필름 질감을 가공 없이 그대로 담은 영화적 내러티브.",
        "texture": "• **더스티 핑크(Dusty Pink) & 흑백 필름 노이즈**: 빛바랜 분홍빛과 거친 필름 그레인의 조화.\n• **유광 플라스틱 케이스 vs 무광 마이너 속지**: 케이스를 열었을 때 손끝에 닿는 촉각적 대비감 연출.",
        "director_note": "💡 *\"단순히 예쁜 커버를 그리는 게 아니라, 관객이 앨범을 손에 쥐는 순간 '특정한 시대의 기억'을 소환하는 물리적 매개체(오브제)를 만드는 작업입니다.\""
    },
    {
        "title": "🎨 [아트 디렉터스 컷] 샤이니(SHINee) - '1 of 1'",
        "concept": "90년대 뉴잭스윙의 부활: 한정판 카세트테이프 패키징",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/bts_bst.png",
        "color": 0xFFD700,
        "typography": "• **90s 볼드 산세리프 & 사선 블로킹**: 90년대 스트리트 패션 매거진에서 튀어나온 듯한 두텁고 당당한 타이포그래피.\n• **형광 볼드 넘버링**: 원색 대비를 이용해 숫자를 메인 그래픽 엘리먼트로 활용.",
        "packaging": "• **실제 재생 가능한 한정판 오리지널 카세트테이프**: 음원 스트리밍 시대에 아날로그 마그네틱 테이프의 플레이어 노스탤지어를 직격.\n• **빈티지 플라스틱 쥬얼 케이스**: 카세트테이프 특유의 투명 경첩 케이스와 접이식 J-카드 가사집 완벽 재현.",
        "texture": "• **프라이머리 컬러(Primary Colors)**: 순도 높은 옐로우, 레드, 블루의 강렬한 보색 충돌.\n• **매끄러운 아크릴 플라스틱 & 마그네틱 테이프 리본 질감**.",
        "director_note": "💡 *\"레트로 콘셉트의 성공 여부는 디테일에 있습니다. 폰트만 복고풍으로 쓰는 데 그치지 않고, 그 시대의 물리적 포맷(카세트테이프)까지 완벽하게 소환해야 진짜 설득력이 생깁니다.\""
    },
    {
        "title": "🎨 [아트 디렉터스 컷] 아이브(IVE) - 'I'VE MINE'",
        "concept": "트리플 타이틀 3색 일러스트레이션 & 실버 포일 스탬핑",
        "image_url": "https://raw.githubusercontent.com/hyeonyeong12/-/main/images/ive_iam.png",
        "color": 0x9933FF,
        "typography": "• **우아한 클래식 모던 세리프**: 고전적 서양화풍과 조화를 이루는 날렵하고 세련된 세리프 폰트.\n• **실버박(Silver Foil) 후가공**: 로고에 은박을 압인하여 각도에 따라 영롱하게 빛나는 고급스러운 존재감 부여.",
        "packaging": "• **명화 액자(Picture Frame) 모티브 하드커버**: 세 개의 타이틀곡 무드를 세 가지 독창적인 일러스트레이터와의 협업으로 완성한 갤러리형 패키지.\n• **하이브리드 아트워크**: 실사 사진과 몽환적 회화 기법을 콜라주하여 신비로운 동화적 깊이감 연출.",
        "texture": "• **라벤더 퍼플, 소프트 로즈, 딥 네이비**: 각 타이틀곡의 서사를 상징하는 3색 테마 톤앤매너.\n• **고평량 고급 한지/텍스처지 속지**: 종이 본연의 결이 느껴지는 프리미엄 촉감.",
        "director_note": "💡 *\"다양한 음악적 스펙트럼을 가진 멀티 타이틀 앨범일수록, 앨범 커버를 아트 전시회의 연작 시리즈처럼 기획하면 팬들에게 수집의 즐거움과 브랜드 가치를 동시에 줍니다.\""
    }
]

def send_album_art_analysis():
    if not WEBHOOK_URL:
        print("❌ DISCORD_ALBUM_ART_WEBHOOK_URL 환경 변수가 없습니다.")
        return

    item = random.choice(ALBUM_ART_ARCHIVE)
    today = datetime.now().strftime("%Y년 %m월 %d일")

    embed = {
        "title": item["title"],
        "description": f"**비주얼 콘셉트:** {item['concept']}\n*30년 차 디렉터가 분석하는 K-POP 앨범 아트 & 패키징 미학*",
        "color": item["color"],
        "image": {"url": item["image_url"]},
        "fields": [
            {"name": "🔤 타이포그래피 & 로고 미학", "value": item["typography"], "inline": False},
            {"name": "📦 피지컬 패키징 & 오브제 혁신", "value": item["packaging"], "inline": False},
            {"name": "🎨 컬러 그레이딩 & 질감 (Texture)", "value": item["texture"], "inline": False},
            {"name": "💡 아트 디렉터 실무 노트", "value": item["director_note"], "inline": False}
        ],
        "footer": {
            "text": f"Pickle Album Art & Visual Identity Archive • {today}"
        }
    }

    payload = {
        "username": "앨범 아트 디렉터 아카이브",
        "avatar_url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=128&auto=format&fit=crop&q=80",
        "content": "오늘의 앨범 아트 & 비주얼 아이덴티티 아카이브가 도착했습니다! 🎨",
        "embeds": [embed]
    }

    resp = requests.post(WEBHOOK_URL, json=payload)
    if resp.status_code == 204:
        print("✅ 앨범아트 채널 전송 성공!")
    else:
        print(f"⚠️ 전송 실패: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    send_album_art_analysis()
