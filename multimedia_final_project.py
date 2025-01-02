import numpy as np
import librosa
import soundfile as sf

import subprocess
import os

def speed_up_video(input_file, output_file, speed_factor):
    # 確認檔案是否存在
    if not os.path.exists(input_file):
        print(f"輸入檔案不存在: {input_file}")
        return

    #FFMPEG命令
    command = [
        "ffmpeg",
        "-i", input_file,  #輸入檔案
        "-filter:v", f"setpts=PTS/{speed_factor}",  # 設定影片播放速度
        "-filter:a", f"atempo={speed_factor}",  # 設定音訊播放速度
        "-y",  # 覆蓋輸出檔案
        output_file
    ]

    try:
        # FFMPEG 指令
        print("執行 FFMPEG 指令...")
        subprocess.run(command, check=True)
        print(f"影片處理完成，輸出檔案: {output_file}")
    except subprocess.CalledProcessError as e:
        # 發生錯誤時顯示錯誤訊息
        print("處理影片時發生錯誤:", e)

def phase_vocoder(audio_path, speed_factor, output_path):
    # 確認倍數 (0.1-2.0)
    if not (0.1 <= speed_factor <= 2.0):
        raise ValueError("Speed factor must be between 0.1 and 2.0.")

    # 加載音訊檔案
    y, sr = librosa.load(audio_path, sr=None) 

    # 計算短時傅立葉變換 (STFT)
    stft = librosa.stft(y)

    # 相位聲碼器進行時間壓縮或拉伸
    stft_stretched = librosa.phase_vocoder(stft, rate=speed_factor)

    # 將 STFT 轉回時域信號
    y_stretched = librosa.istft(stft_stretched)

    # 保存處理後的音訊檔案
    sf.write(output_path, y_stretched, sr)

    # 顯示處理完成訊息
    print(f"Processed audio saved to {output_path}")

def change_speed_with_frequency(audio_path, speed_factor, output_path):
    # 確認倍數(0.1-2.0)
    if not (0.1 <= speed_factor <= 2.0):
        raise ValueError("Speed factor must be between 0.1 and 2.0.")

    # 加載音訊檔案
    y, sr = librosa.load(audio_path, sr=None)

    # 使用重新取樣改變速度和頻率
    y_stretched = librosa.resample(y, orig_sr=sr, target_sr=int(sr * 1 / speed_factor))

    # 保存處理後的音訊檔案
    sf.write(output_path, y_stretched, sr)

    # 顯示處理完成訊息
    print(f"Processed audio with speed adjustment saved to {output_path}")



try:
    input_audio = "./sample_audio.mp3"  
    output_audio_vo = "./output_audio_vo.wav"  # 輸出的檔案路徑
    output_audio_normal = "./output_audio_normal.wav"  # 改變速度和頻率後的輸出檔案路徑
    speed = 2  # 設定速度調整倍數
    # 使用相位聲碼器處理音訊
    phase_vocoder(input_audio, speed, output_audio_vo)

    # 改變速度和頻率處理音訊
    change_speed_with_frequency(input_audio, speed, output_audio_normal)

    # 預設參數
    input_video = "./sample_video.mp4"  # 輸入影片檔案路徑
    output_video = "./output_video.mp4"  # 輸出影片檔案路徑

    # 呼叫函數處理影片
    speed_up_video(input_video, output_video, speed)
except Exception as e:
    # 顯示錯誤訊息
    print(f"An error occurred: {e}")