import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBhKjgnTC81VGBLHS6bStpxzxrC7iRz42M")
# Create the model
generation_config = {
  "temperature": 0.55,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Tujuan\nMengembangkan sistem yang dapat membaca dokumen yang diunggah oleh pengguna dan menghasilkan output yang sesuai berdasarkan permintaan pengguna.\n\nLangkah-langkah:\nPengunggahan Dokumen:\n\nMinta pengguna untuk mengunggah dokumen dalam format yang didukung (PDF, DOCX, TXT, dsb.).\nVerifikasi dan simpan dokumen yang diunggah ke dalam sistem untuk diproses lebih lanjut.\nEkstraksi Teks:\n\nGunakan pustaka pemrosesan teks untuk mengekstrak teks dari dokumen yang diunggah.\nLakukan pembersihan teks untuk menghilangkan karakter khusus dan elemen yang tidak relevan.\nPenerimaan Input Pengguna:\n\nTanyakan kepada pengguna tentang informasi spesifik yang ingin dihasilkan dari dokumen (misalnya, ringkasan, analisis, pertanyaan, dsb.).\nSimpan input pengguna untuk digunakan dalam langkah pemrosesan berikutnya.\nPemrosesan Permintaan:\n\nBerdasarkan input pengguna, gunakan model pemrosesan bahasa alami (NLP) untuk:\nMenghasilkan ringkasan dari dokumen.\nMenjawab pertanyaan spesifik terkait konten dokumen.\nMenyediakan analisis atau insight dari informasi yang terdapat dalam dokumen.\nMenghasilkan konten baru yang relevan berdasarkan data yang ada.\nGenerasi Output:\n\nFormat output sesuai dengan permintaan pengguna (teks, tabel, grafik, dsb.).\nJika diperlukan, sertakan referensi ke bagian tertentu dalam dokumen asli yang relevan dengan output yang dihasilkan.\nTampilan Hasil:\n\nTampilkan hasil output kepada pengguna dengan cara yang jelas dan terstruktur.\nBerikan opsi kepada pengguna untuk mengunduh hasil dalam format yang diinginkan (misalnya, PDF, DOCX, dsb.).\nUmpan Balik dan Iterasi:\n\nMinta umpan balik dari pengguna mengenai hasil yang dihasilkan.\nJika pengguna memiliki permintaan tambahan atau revisi, ulangi langkah pemrosesan sesuai kebutuhan.",
)

chat_session = model.start_chat(
  history=[
  ]
)

def generate_ai_response(user_input):
  response = chat_session.send_message(user_input)
  print(response.text)
  return response
