# 

# \# FFmpeg\\\_Based\\\_Time-Domain\\\_Audio\\\_Stretching

# 

# \## 專案介紹 

# 

# 此為〈多媒體技術概論〉之期末報告，解析影片與音訊加速的原理，並透過 FFmpeg 實際展示效果。

# 本專案示範如何使用 \*\*FFmpeg\*\* 搭配 \*\*Librosa\*\* 與 \*\*SoundFile\*\*，對影片與音訊進行時間領域的壓縮與伸展 (Time-Domain Audio Stretching)。

# 程式中實作了三種不同方式來調整速度：

# 

# 1\. \*\*影片與音訊加速 (FFmpeg)\*\*

# 

# &nbsp;  \* 使用 `ffmpeg` 的 `setpts` 與 `atempo` 濾鏡，直接對影片與音訊做同步加速/減速。

# 

# 2\. \*\*相位聲碼器 (Phase Vocoder, Librosa)\*\*

# 

# &nbsp;  \* 利用短時傅立葉轉換 (STFT) 與相位聲碼器演算法，調整音訊的播放速度而不改變音高。

# 

# 3\. \*\*重新取樣 (Resampling, Librosa)\*\*

# 

# &nbsp;  \* 透過改變取樣率達成速度與音高的同步變化。

# 

# \### 專案結構

# 

# ```

# .

# ├── sample\_audio.mp3        # 範例音訊檔

# ├── sample\_video.mp4        # 範例影片檔

# ├── output\_audio\_vo.wav     # Phase Vocoder 處理後的音訊

# ├── output\_audio\_normal.wav # Resample 處理後的音訊

# ├── output\_video.mp4        # FFmpeg 處理後的影片

# └── main.py                 # 主程式

# ```

# 

# \### 使用方式

# 

# 1\. 安裝必要套件：

# 

# &nbsp;  ```bash

# &nbsp;  pip install numpy librosa soundfile

# &nbsp;  ```

# 

# &nbsp;  並確保本機有安裝 \*\*FFmpeg\*\*。

# 

# 2\. 執行程式：

# 

# &nbsp;  ```bash

# &nbsp;  python main.py

# &nbsp;  ```

# 

# 3\. 輸出檔案會自動生成在專案目錄下。



