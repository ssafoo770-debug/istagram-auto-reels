import os
import time
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, ColorClip, CompositeVideoClip
from instagrapi import Client

# ===============================
# إعدادات الحساب والنص
# ===============================
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

LEGAL_TEXT = (
    "احذر! الابتزاز الإلكتروني جريمة يعاقب عليها القانون العراقي بشدة. "
    "لا تضحي بنفسك وتخضع للمبتز، توجه فوراً إلى الجهات المختصة واستشر محاميك."
)

CAPTION_TEXT = (
    "الوعي القانوني حمايتك! \n\n"
    "لا تتردد في طلب المساعدة القانونية فور تعرضك لأي ابتزاز.\n\n"
    "#قانون #العراق #الوعي_القانوني #حامي #سيف_سامر"
)

def generate_video():
    print("1. جاري توليد ملف الصوت من النص...")
    tts = gTTS(text=LEGAL_TEXT, lang='ar')
    audio_path = "legal_audio.mp3"
    tts.save(audio_path)
    
    print("2. جاري إنشاء وتصميم فيديو الريلز...")
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    
    bg_clip = ColorClip(size=(1080, 1920), color=(20, 20, 40), duration=duration)
    video = bg_clip.set_audio(audio_clip)
    video_path = "final_reel.mp4"
    
    video.write_videofile(video_path, fps=24, codec="libx264", audio_codec="aac")
    print("3. تم إنشاء الفيديو بنجاح!")
    return video_path

def upload_to_instagram(video_path):
    print("4. جاري تسجيل الدخول إلى إنستغرام...")
    cl = Client()
    
    try:
        cl.login(USERNAME, PASSWORD)
        print("تم تسجيل الدخول بنجاح!")
        
        print("5. جاري رفع الفيديو كـ (Reel) إلى إنستغرام...")
        cl.clip_upload(
            video_path,
            caption=CAPTION_TEXT
        )
        print("تم نشر الريل بنجاح على إنستغرام!")
        
    except Exception as e:
        print(f"حدث خطأ أثناء تسجيل الدخول أو النشر: {e}")
        raise e

if __name__ == "__main__":
    if not USERNAME or not PASSWORD:
        print("خطأ: يرجى التأكد من ضبط متغيرات IG_USERNAME و IG_PASSWORD في Secrets")
    else:
        vid_file = generate_video()
        upload_to_instagram(vid_file)
