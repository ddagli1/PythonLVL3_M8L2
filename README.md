# 🚀 Bilgisayarı Hızlandıracak Python Scriptleri

> Python ile sistem kaynaklarını akıllıca yönet, bilgisayarını zirveye taşı.

---

## 📌 Genel Bakış

Bilgisayarın takılmadan ve sağlıklı çalışması için donanım kaynaklarının (işlemci, RAM vb.) doğru yönetilmesi şarttır. Python, bu kaynakları kendi kendine takip eden, analiz eden ve optimize eden scriptler yazmak için en ideal araçtır.

| Sorun | Çözüm | Araç |
|-------|-------|------|
| Kaynaklar düzensiz kullanılırsa sistem yavaşlar veya donar | Kaynakları otomatik takip eden scriptler yazmak | Python |

---

## 🧠 Sistem Kaynaklarını Tanıyalım

### 🍳 1. CPU (İşlemci) — Mutfaktaki Aşçı

- **Nedir?** Bilgisayarın asıl işini yapan birimdir; tüm komutları o yürütür.
- **Nasıl çalışır?** Yemek tarifini (kodları) okur ve yemeği pişirir.
- **Python ile:** Aşçının ne kadar yorulduğunu ve sıcaklığını takip edebiliriz.

### 🥦 2. RAM (Bellek) — Mutfak Tezgahı

- **Nedir?** O an üzerinde çalışılan işlerin tutulduğu geçici alandır.
- **Nasıl çalışır?** Tezgah dolarsa işler yavaşlar.
- **Python ile:** Gereksiz yer kaplayan bellek sızıntılarını tespit edebiliriz.

### 🗄️ 3. Depolama (Storage) — Kiler / Buzdolabı

- **Nedir?** Dosyaların kalıcı olarak saklandığı birimdir.
- **Nasıl çalışır?** Kiler dolarsa içeriye yeni bir şey koyamazsın.
- **Python ile:** Disk doluluk oranını otomatik kontrol edebiliriz.

### 🍲 4. Çalışan Süreçler — Ocaktaki Tencereler

- **Nedir?** Arka planda açık olan tüm programlar.
- **Nasıl çalışır?** Aynı anda 5 tencere kaynıyorsa mutfak karışabilir.
- **Python ile:** Hangi sürecin fazla kaynak tükettiğini izleyip müdahale edebiliriz.

> 💡 **Özet:** Bu dörtlü arasındaki dengeyi iyi kurmak gerekir. Python bize bu mutfağın **"şefi"** olma imkânı verir.

---

## ❓ Neden Kontrol Etmeliyiz?

Bilgisayar kaynaklarını izlemek yalnızca hız kazandırmaz:

- **Çökmeleri engeller** — Sistemin aniden donmasını önler.
- **Ömrü uzatır** — Aşırı ısınmayı engelleyerek parçaların daha uzun süre sağlam kalmasını sağlar.

---

## 🐍 Neden Python?

- **Basit sözdizimi** — Karmaşık kodlar yerine, İngilizce konuşur gibi komutlar yazılır.
- **Platform bağımsız** — Yazılan kod hem Windows'ta hem macOS'ta hem de Linux'ta çalışır.
- **Geniş ekosistem** — Sistem yönetimi için hazır kütüphaneler mevcuttur.

---

## 📦 Kullanılan Kütüphaneler

| Kütüphane | Açıklama |
|-----------|----------|
| `psutil` | CPU, RAM, disk, ağ gibi genel sistem durumunu izler |
| `GPUtil` | GPU (ekran kartı) performansını ölçer |
| `os` | İşletim sistemi dosyalarına ve derinliklerine köprü kurar |

### Kurulum

```bash
pip install psutil GPUtil
```

---

## ⚖️ İki Yöntemin Karşılaştırması

### ❌ Python Olmadan (Eski Usul)

Fabrikayı elde kâğıt kalemle tek tek gezmek gibidir.

- Sürekli manuel takip gerektirir (Görev Yöneticisi / Task Manager)
- Sorun oluştuğunda sistemin otomatik önlem alması zordur
- Yalnızca işletim sisteminin izin verdiği kadarıyla sınırlıdır

### ✅ Python İle (Modern ve Akıllı Usul)

Fabrikayı kameralar ve akıllı sensörlerle donatıp her şeyi merkezden izlemek gibidir.

- **Kendi kendine çalışır** — Sen uyurken bile arka planda sistemi izler; sorun olduğunda uyarı gönderir.
- **Esnektir** — "RAM dolduğunda şu programı kapat, işlemci ısındığında uyarı ver" gibi özel kurallar tanımlanabilir.
- **Her yerde geçerli** — Yazılan akıllı sistem her bilgisayarda kolayca çalışır.

---

## 🗂️ Proje Yapısı

```
📁 sistem-yoneticisi/
├── 📄 README.md           # Bu dosya
├── 📄 cpu_monitor.py      # CPU kullanımı ve sıcaklık takibi
├── 📄 ram_monitor.py      # RAM kullanımı ve bellek sızıntısı tespiti
├── 📄 disk_monitor.py     # Disk doluluk oranı kontrolü
├── 📄 process_manager.py  # Çalışan süreçleri izleme ve müdahale
└── 📄 system_dashboard.py # Tüm kaynakları tek ekranda izleme
```

---

## 🚀 Hızlı Başlangıç

```python
import psutil

# CPU kullanım oranı
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Kullanımı: %{cpu}")

# RAM durumu
ram = psutil.virtual_memory()
print(f"RAM Kullanımı: %{ram.percent}")

# Disk durumu
disk = psutil.disk_usage('/')
print(f"Disk Kullanımı: %{disk.percent}")
```

---

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak istersen:

1. Bu repoyu **fork**'la
2. Yeni bir branch oluştur (`git checkout -b ozellik/yeni-script`)
3. Değişikliklerini commit'le (`git commit -m 'Yeni: GPU sıcaklık uyarısı eklendi'`)
4. Branch'ini push'la (`git push origin ozellik/yeni-script`)
5. Bir **Pull Request** aç

---

## 📄 Lisans

Bu proje MIT lisansı altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---

<p align="center">
  ⚡ Python ile bilgisayarının tam kontrolünü ele geçir.
</p>
