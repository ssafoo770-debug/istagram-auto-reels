import os
import time
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, ColorClip, CompositeVideoClip
from instagrapi import Client

# ===============================
# إعدادات الحساب والنص
# لضمان السرية التامة GitHub Secrets تسحب بيانات الحساب بأمان من #
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

# النص التوعوي القانوني الخاص بسلسلة الوعي القانوني ضد الابتزاز #
LEGAL_TEXT = (
    " احذر! الابتزاز الإلكتروني جريمة يعاقب عليها القانون العراقي بشدة."
    "لا تضحي بنفسك وتخضع للمبتز، توجه فوراً إلى الجهات المختصة واستتر محاميك."
)

CAPTION_TEXT = (
    "الوعي القانوني حمايتك! \n\n"
    "لا تتردد في طلب المساعدة القانونية فور تعرضك لأي ابتزاز.\n\n"
    "#قانون #العراق #الوعي_القانوني #حامي #سيف_سامر"
)
