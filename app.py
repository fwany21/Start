import streamlit as st
import time
import random

# 페이지 제목
st.title("⚠️ 브라우저 내장 경고음 테스트")

# 메시지 출력을 위한 공간 생성
message_placeholder = st.empty()

# 버튼 클릭 시 실행
if st.button("시작"):
    message_placeholder.text("대기 중...")

        # 1~15초 랜덤 대기
    wait_time = random.randint(1, 15)
    time.sleep(wait_time)

                    # JavaScript를 활용한 브라우저 내장 경고음
    beep_js = """
        <script>
            function beep() {
                var ctx = new (window.AudioContext || window.webkitAudioContext)();
                var oscillator = ctx.createOscillator();
                oscillator.type = "square";
                oscillator.frequency.setValueAtTime(1000, ctx.currentTime); // 1000Hz 경고음
                oscillator.connect(ctx.destination);
                oscillator.start();
                setTimeout(() => oscillator.stop(), 200); // 0.2초 동안 소리
            }
            beep();
        </script>
    """

# 메시지 변경 및 경고음 실행
message_placeholder.text("🚨 경고음 발생!")
st.markdown(beep_js, unsafe_allow_html=True)