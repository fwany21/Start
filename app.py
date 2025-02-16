import streamlit as st
import time
import random

# 페이지 제목
st.title("Streaming 시작")

# 메시지 출력을 위한 공간 생성
message_placeholder = st.empty()

# 버튼 클릭 시 실행
if st.button("시작"):
    message_placeholder.text("대기 중...")

        # 1~15초 랜덤 대기
            wait_time = random.randint(1, 15)
                time.sleep(wait_time)

                    # HTML을 사용하여 오디오 자동 재생
                        audio_html = """
                            <audio autoplay>
                                    <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
                                            브라우저가 오디오 태그를 지원하지 않습니다.
                                                </audio>
                                                    """

                                                        # 메시지 변경 및 오디오 재생
                                                            message_placeholder.text("🚀 시작!")
                                                                st.markdown(audio_html, unsafe_allow_html=True)