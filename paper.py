from groq import Groq

def parafrase(awal):
    # Prompt untuk generate kalimat
    prompt = """
    Buatkan satu variasi kalimat deskripsi nilai rapor dari kalimat berikut.
    
    Kalimat:
    "{sentence}"

    Ketentuan:
    - Bahasa Indonesia formal dan natural
    - Variasikan struktur kalimat
    - Gunakan sinonim yang sesuai konteks pendidikan
    - Tetap mempertahankan makna evaluatif
    - Hindari pengulangan kata yang sama
    - Tidak perlu memberikan kalimat tambahan apapun
    """
    prompt = prompt.format(sentence=awal)
    # Request ke model
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=5000
    )

    # Ambil hasil
    return response.choices[0].message.content

def parafrase_saran(awal):
    # Prompt untuk generate kalimat
    prompt = """
    Anda adalah asisten pendidikan. Buatlah pesan singkat yang positif dan konstruktif untuk seorang siswa berdasarkan nilai ujian, kegiatan ekstrakurikuler, dan kehadiran.

    Input:
    {sentence}

    Aturan:
    - Output harus tepat 3 kalimat.
    - Kalimat 1: Ringkasan prestasi akademik.
    - Kalimat 2: Ringkasan partisipasi ekstrakurikuler dan kehadiran.
    - Kalimat 3: Berikan 1 saran konstruktif untuk peningkatan.
    - Gunakan bahasa yang ramah dan mendorong.
    - Cocok untuk dicantumkan di rapor sekolah.
    """
    prompt = prompt.format(sentence=awal)
    # Request ke model
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=5000
    )

    # Ambil hasil
    return response.choices[0].message.content

client = Groq(api_key="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")
kalimat_deskripsi = "Pemahaman Ananda Ipin terhadap materi Matematika tergolong cukup, namun penguasaan materi bilangan pecahan, perkalian dan pembagian pecahan masih perlu ditingkatkan."
print(parafrase(kalimat_deskripsi))
print("----------------------------------")

kalimat_deskripsi = "Ananda Ipin cukup aktif dan menunjukkan hasil yang baik dalam kegiatan Pramuka."
print(parafrase(kalimat_deskripsi))
print("----------------------------------")

kalimat_deskripsi = "Ananda Ipin memiliki tingkat kehadiran yang cukup dan perlu perbaikan."
print(parafrase(kalimat_deskripsi))
print("----------------------------------")

kalimat_deskripsi = """
Penguasaan Ananda Ipin terhadap topik Matematika berada pada level yang memadai, namun kemampuan dalam bilangan pecahan serta operasi perkalian dan pembagian pecahan masih memerlukan peningkatan.
Ananda Ipin memperlihatkan partisipasi yang signifikan serta pencapaian memuaskan dalam aktivitas Pramuka.
Ananda Ipin menunjukkan kehadiran yang memadai namun masih memerlukan peningkatan.
"""
print(parafrase_saran(kalimat_deskripsi))
print("----------------------------------")
