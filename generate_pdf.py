import os
import urllib.request
from fpdf import FPDF, XPos, YPos

ICONS_DIR = "icons"
ICON_URLS = {
    "html5": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
    "css3": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
    "javascript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    "c": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg",
    "python": "https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png",
}

def download_fonts():
    font_url = "https://github.com/google/fonts/raw/main/ofl/notosanskr/NanumGothic-Regular.ttf"
    font_bold_url = "https://github.com/google/fonts/raw/main/ofl/notosanskr/NanumGothic-Bold.ttf"
    if not os.path.exists("NanumGothic.ttf"):
        print("Downloading NanumGothic Regular...")
        urllib.request.urlretrieve(font_url, "NanumGothic.ttf")
    if not os.path.exists("NanumGothic-Bold.ttf"):
        print("Downloading NanumGothic Bold...")
        urllib.request.urlretrieve(font_bold_url, "NanumGothic-Bold.ttf")

def download_icons():
    os.makedirs(ICONS_DIR, exist_ok=True)
    for name, url in ICON_URLS.items():
        ext = url.split('.')[-1]
        path = os.path.join(ICONS_DIR, f"{name}.{ext}")
        if not os.path.exists(path):
            print(f"Downloading {name} icon...")
            urllib.request.urlretrieve(url, path)

# 16:9 landscape (338.67mm x 190.5mm)
PW = 338.67
PH = 190.5

class PortfolioPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="L", unit="mm", format=(PH, PW))
        self.set_auto_page_break(auto=False)

def create_pdf():
    pdf = PortfolioPDF()
    pdf.add_font("NanumGothic", style="", fname="NanumGothic.ttf")
    pdf.add_font("NanumGothic", style="B", fname="NanumGothic-Bold.ttf")

    nav_labels = ["About", "Projects", "Stacks"]
    nav_y = 12
    nav_w = 35
    nav_gap = 5
    total_nav_w = nav_w * len(nav_labels) + nav_gap * (len(nav_labels) - 1)
    nav_start_x = (PW - total_nav_w) / 2

    def draw_nav(active_index):
        for i, label in enumerate(nav_labels):
            x = nav_start_x + i * (nav_w + nav_gap)
            if i == active_index:
                pdf.set_fill_color(0, 0, 0)
                pdf.set_text_color(255, 255, 255)
            else:
                pdf.set_fill_color(245, 245, 245)
                pdf.set_text_color(100, 100, 100)
            pdf.set_font("NanumGothic", size=11)
            pdf.set_xy(x, nav_y)
            pdf.cell(nav_w, 9, label, align="C", fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_text_color(0, 0, 0)

    # ===========================
    # Page 1: About
    # ===========================
    pdf.add_page()
    draw_nav(0)

    pdf.set_font("NanumGothic", style="B", size=36)
    pdf.set_xy(10, PH / 2 - 25)
    pdf.cell(PW - 20, 22, "안녕하세요", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("NanumGothic", style="B", size=26)
    pdf.cell(PW - 20, 18, "선린인터넷 고등학교 소속 이진헌입니다", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ===========================
    # Page 2: Projects
    # ===========================
    pdf.add_page()
    draw_nav(1)

    pdf.set_font("NanumGothic", style="B", size=24)
    pdf.set_xy(10, 32)
    pdf.cell(PW - 20, 14, "Projects", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)

    projects = [
        {
            "title": "Minecraft 로그인 자동화 매크로",
            "desc": "Python과 Selenium을 활용하여 로그인 과정을 자동화하고, 희귀 닉네임을 사용하기 위해 닉네임 변경을 반복하는 매크로 프로그램입니다.",
            "video": "https://youtu.be/1f42rbSqGUw",
            "site": None
        },
        {
            "title": "콘텐츠 허브",
            "desc": "Python, PySide6, SQLite을 활용한 유튜브, 네이버 웹툰, 카카오페이지에서 구독 중인 채널·작품의 최신 업로드를 한 곳에서 확인할 수 있는 데스크톱 알림 오버레이입니다. 유튜브는 구글 계정 연동, 네이버 웹툰과 카카오페이지는 링크만 등록하면 새 업로드가 생길 때마다 자동으로 알려줍니다.",
            "video": "https://youtu.be/tSu61Uw2l4o",
            "site": None
        },
        {
            "title": "진법 변환기",
            "desc": "가장 자주 사용되는 2, 8, 10, 16진수를 손쉽게 상호 변환할 수 있는 심플한 웹 기반 진법 변환기입니다. 숫자를 입력하는 즉시 결괏값이 실시간으로 표시됩니다.",
            "video": "https://youtu.be/4ENZtwrMXXI",
            "site": None
        },
        {
            "title": "Sumi",
            "desc": "discord.js를 활용한 디스코드 통화방의 음성 대화를 실시간으로 녹음하여 텍스트로 변환하고 핵심 내용을 요약해 주는 디스코드 봇입니다. 통화가 끝난 직후 OpenAI의 Whisper 및 GPT 모델을 활용해 회의록 수준의 깔끔한 요약본을 전송합니다.",
            "video": "",
            "site": None
        }
    ]

    # 3 cards side by side, vertically centered
    margin = 40
    gap = 12
    card_count = len(projects)
    card_w = (PW - margin * 2 - gap * (card_count - 1)) / card_count
    card_h = 100
    card_top = (PH - card_h) / 2 + 10  # vertically center with slight offset for title

    for idx, proj in enumerate(projects):
        cx = margin + idx * (card_w + gap)

        # Card border
        pdf.set_draw_color(220, 220, 220)
        pdf.rect(cx, card_top, card_w, card_h)

        # Title
        pdf.set_xy(cx + 10, card_top + 10)
        pdf.set_font("NanumGothic", style="B", size=13)
            
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(card_w - 20, 7, proj["title"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        title_bottom = pdf.get_y()

        # Description
        pdf.set_xy(cx + 10, title_bottom + 4)
        pdf.set_font("NanumGothic", size=9)
        pdf.set_text_color(85, 85, 85)
        pdf.multi_cell(card_w - 20, 5.5, proj["desc"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Separator line
        sep_y = card_top + card_h - 24
        pdf.set_draw_color(235, 235, 235)
        pdf.line(cx + 10, sep_y, cx + card_w - 10, sep_y)

        # Links at bottom of card
        link_y = sep_y + 4
        pdf.set_font("helvetica", size=8)
        pdf.set_text_color(0, 102, 204) # Blue color for links
        pdf.set_xy(cx + 10, link_y)
        if proj.get("video"):
            pdf.cell(card_w - 20, 6, proj["video"], link=proj["video"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        if proj.get("site"):
            if not proj.get("video"):
                pdf.set_xy(cx + 10, link_y)
            else:
                pdf.set_xy(cx + 10, link_y + 6)
            pdf.cell(card_w - 20, 6, proj["site"], link=proj["site"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Tag (if exists) rendered at the bottom right
        if proj.get("tag"):
            pdf.set_font("NanumGothic", size=7)
            tag_text = proj["tag"]
            tag_tw = pdf.get_string_width(tag_text) + 6
            tag_x = cx + card_w - 10 - tag_tw
            tag_y = sep_y + 6
            pdf.set_xy(tag_x, tag_y)
            pdf.set_fill_color(0, 0, 0)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(tag_tw, 5, tag_text, align="C", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ===========================
    # Page 3: Stacks
    # ===========================
    pdf.add_page()
    draw_nav(2)

    pdf.set_font("NanumGothic", style="B", size=24)
    pdf.set_xy(10, 32)
    pdf.cell(PW - 20, 14, "Tech Stacks", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    stacks = [
        {"name": "HTML", "icon": os.path.join(ICONS_DIR, "html5.svg")},
        {"name": "CSS", "icon": os.path.join(ICONS_DIR, "css3.svg")},
        {"name": "JavaScript", "icon": os.path.join(ICONS_DIR, "javascript.svg")},
        {"name": "C", "icon": os.path.join(ICONS_DIR, "c.svg")},
        {"name": "Python", "icon": os.path.join(ICONS_DIR, "python.png")},
    ]

    icon_size = 30
    item_w = 60
    total_w = item_w * len(stacks)
    start_x = (PW - total_w) / 2
    items_y = PH / 2 - 20

    for i, stack in enumerate(stacks):
        cx = start_x + i * item_w + item_w / 2
        icon_x = cx - icon_size / 2
        icon_y = items_y

        pdf.image(stack["icon"], x=icon_x, y=icon_y, w=icon_size, h=icon_size)

        pdf.set_font("NanumGothic", size=11)
        pdf.set_text_color(85, 85, 85)
        label_w = pdf.get_string_width(stack["name"])
        pdf.set_xy(cx - label_w / 2, icon_y + icon_size + 5)
        pdf.cell(label_w, 8, stack["name"], new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.set_text_color(0, 0, 0)
    pdf.output("이진헌_포트폴리오.pdf")
    print("PDF generated: 이진헌_포트폴리오.pdf")

if __name__ == "__main__":
    download_fonts()
    download_icons()
    create_pdf()
