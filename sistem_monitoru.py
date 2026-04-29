# =============================================================================
# 🖥️  SİSTEM KAYNAK MONİTÖRÜ
# =============================================================================
# Bu script, bilgisayarın donanım kaynaklarını (CPU, RAM, Disk, Ağ) gerçek
# zamanlı olarak izlemek ve raporlamak için yazılmıştır.
#
# Kullanım   : python sistem_monitoru.py
# Gereksinim : pip install psutil
# =============================================================================


# -----------------------------------------------------------------------------
# 📦 BÖLÜM 1 — KÜTÜPHANE İÇE AKTARMA (IMPORT)
# -----------------------------------------------------------------------------

import psutil
# psutil (process and system utilities) kütüphanesi:
#   → İşletim sisteminden bağımsız biçimde CPU, RAM, disk, ağ ve çalışan
#     süreçler hakkında bilgi toplamayı sağlar.
#   → Windows, macOS ve Linux'ta aynı şekilde çalışır; platform farkı yoktur.
#   → Harici bir kütüphanedir, yani Python ile birlikte gelmez.
#     Terminale şunu yazarak kurabilirsin:  pip install psutil

import time
# time modülü:
#   → Python'un yerleşik (built-in) zaman modülüdür; kurulum gerektirmez.
#   → Bu scriptte yalnızca time.sleep(saniye) fonksiyonunu kullanıyoruz.
#   → time.sleep(5) → programı 5 saniye boyunca durdurur/bekletir.
#     Bu sayede RAM izleme döngüsü her kontrolden önce bekleme yapabilir.


# =============================================================================
# 📟 BÖLÜM 2 — İŞLEMCİ (CPU) BİLGİLERİ
# =============================================================================

# -----------------------------------------------------------------------------
# 🔢 2A — Çekirdek Sayıları (Mantıksal ve Fiziksel)
# -----------------------------------------------------------------------------

print(f'Mantıksal işlemci sayısı: {psutil.cpu_count()}')
# psutil.cpu_count() → Mantıksal (logical) çekirdek sayısını döndürür.
#
# Mantıksal çekirdek nedir?
#   Hyper-Threading veya SMT (Simultaneous Multi-Threading) gibi teknolojilerle
#   bir fiziksel çekirdek, işletim sistemine iki ayrı çekirdek olarak görünebilir.
#   Örnek: 4 fiziksel çekirdek + Hyper-Threading = 8 mantıksal çekirdek
#
# Neden önemli?
#   Paralel işlem (multi-threading) yazarken kaç iş parçacığı (thread)
#   oluşturabileceğini planlamana yardımcı olur.
#   Python'da threading veya multiprocessing modülleriyle kullanılır.
#
# Döndürdüğü değer türü: int  (örn: 8)

print(f'Fiziksel işlemci sayısı: {psutil.cpu_count(logical=False)}')
# psutil.cpu_count(logical=False) → Gerçek (fiziksel) çekirdek sayısını döndürür.
#
# logical=False parametresi:
#   Varsayılan değer True'dur (mantıksal çekirdekleri sayar).
#   False geçilince yalnızca anakart üzerindeki gerçek çekirdekler sayılır.
#
# İki değer arasındaki farkın yorumu:
#   Mantıksal > Fiziksel  →  CPU'nuz Hyper-Threading destekliyor demektir.
#   İkisi eşitse          →  Hyper-Threading aktif değil ya da desteklenmiyor.
#
# Döndürdüğü değer türü: int  (örn: 4)


# -----------------------------------------------------------------------------
# 📊 2B — Anlık CPU Kullanım Yüzdesi
# -----------------------------------------------------------------------------

print(f'CPU yükü: {psutil.cpu_percent(interval=1)}%')
# psutil.cpu_percent(interval=1) → CPU'nun son 1 saniyedeki ortalama
# kullanım oranını yüzde (%) olarak döndürür. (0.0 ile 100.0 arası float)
#
# interval=1 parametresi ne anlama gelir?
#   Fonksiyon çağrıldığında 1 saniye boyunca CPU'yu ölçer, ardından sonucu verir.
#   Bu bekleme süresi sayesinde daha doğru ve kararlı bir değer elde edilir.
#   interval=None verilirse önceki ölçümle karşılaştırma yapılır ve
#   anlık (bazen yanıltıcı olabilen) bir değer döner.
#
# Değerlerin genel yorumu:
#    0% - 30%  →  Normal kullanım, sistem rahat çalışıyor.
#   30% - 70%  →  Orta yük, sorun yok.
#   70% - 90%  →  Yüksek yük, dikkat edilmeli.
#   90% - 100% →  Kritik! Sistem yanıt vermekte zorlanıyor olabilir.


# =============================================================================
# 💾 BÖLÜM 3 — RAM (BELLEK) BİLGİLERİ
# =============================================================================

ram = psutil.virtual_memory()
# psutil.virtual_memory() → Sistemin fiziksel RAM'i hakkında bilgi içeren
# bir nesne (named tuple) döndürür. Bu nesnenin içindeki alanlar:
#
#   ram.total     → Sistemdeki toplam RAM miktarı (bayt cinsinden, int)
#   ram.available → Hâlâ kullanılabilir olan RAM (bayt cinsinden, int)
#   ram.used      → Şu an kullanımda olan RAM miktarı (bayt cinsinden, int)
#   ram.free      → Tamamen boş olan RAM (bayt cinsinden, int)
#   ram.percent   → Kullanılan RAM'in toplama oranı (yüzde, float)
#                   Hesaplaması: (used / total) * 100
#
# Neden bir değişkene atadık?
#   Aynı fonksiyonu defalarca çağırmak yerine bir kez çağırıp
#   sonucu ram değişkeninde sakladık. Bu hem daha hızlı hem de
#   daha okunabilir bir kod yazmamızı sağlar.

print(f'Kullanılan RAM: {ram.percent}%')
# ram.percent → Kullanılan RAM'in toplam RAM'e oranını yüzde olarak verir.
#
# Örnek çıktı: "Kullanılan RAM: 62.4%"
#
# Bu değer yüksekse (genellikle >80%) sistem yavaşlamaya başlayabilir.
# Neden? RAM yetersiz kaldığında işletim sistemi disk üzerindeki "swap"
# alanına yazmaya başlar. Diske yazma, RAM'e göre çok daha yavaştır;
# bu durum ciddi performans düşüşüne yol açar.


# =============================================================================
# 💿 BÖLÜM 4 — DİSK BİLGİLERİ
# =============================================================================

disk = psutil.disk_usage('/')
# psutil.disk_usage(yol) → Belirtilen dizinin (disk bölümünün) kullanım
# bilgilerini içeren bir nesne (named tuple) döndürür.
#
# '/' parametresi:
#   Linux ve macOS'ta ana (root) diski temsil eder.
#   Windows'ta bu yol çalışmaz! Windows için şunu kullan:
#     psutil.disk_usage('C:\\')
#
# Döndürdüğü nesnenin alanları:
#   disk.total   → Toplam disk kapasitesi (bayt cinsinden)
#   disk.used    → Kullanılan disk alanı (bayt cinsinden)
#   disk.free    → Boş disk alanı (bayt cinsinden)
#   disk.percent → Kullanılan alanın toplama yüzdesi (float)

print(f'Toplam disk kapasitesi: {disk.total // (1024 ** 3)} GB')
# disk.total → Toplam disk kapasitesi bayt (byte) cinsindendir.
# Bunu GB'a çevirmek için şu dönüşüm uygulanır:
#
#   1 KB =       1.024  Byte
#   1 MB =   1.048.576  Byte  =  1024²
#   1 GB = 1.073.741.824 Byte  =  1024³  →  1024 ** 3
#
# // (tam bölme / floor division) operatörü:
#   Normal bölme (/)  ondalıklı sayı döndürür:  465.76
#   Tam bölme (//)    ondalık kısmı atar:         465
#   Disk boyutunu tamsayı göstermek daha okunabilirdir.

print(f'Kullanılan: {disk.used // (1024 ** 3)} GB')
# disk.used → Dosyalar, programlar ve işletim sistemi tarafından kullanılan
# disk alanıdır. Aynı GB dönüşüm mantığı burada da uygulanıyor.

print(f'Boş disk alanı: {disk.free // (1024 ** 3)} GB')
# disk.free → Yeni dosya ve program yazmak için kullanılabilecek boş alan.
#
# Mantık kontrolü: disk.total ≈ disk.used + disk.free  (yaklaşık eşitlik)
#
# ⚠️ Dikkat: Boş alan kritik seviyeye düşerse (<5 GB) işletim sistemi
#    geçici dosya yazamaz hale gelir ve sistem kilitlenebilir.
#    Bu değerin düzenli takip edilmesi önerilir.


# =============================================================================
# ⚙️  BÖLÜM 5 — ÇALIŞAN İŞLEMLER (PROCESSES)
# =============================================================================

print("Çalışan işlemlerin listesi:")
# Başlık satırı — altındaki for döngüsünde listelenecek
# süreçlerin üstüne bir etiket koyuyoruz.

for process in psutil.process_iter(['name']):
    print(process.info)
# psutil.process_iter(['name']) → Sistemde o an çalışan her bir süreci
# (process) tek tek dolaşmamızı sağlayan bir generator (üreteç) döndürür.
#
# ['name'] parametresi — hangi bilgileri istediğimizi belirtir:
#   Yalnızca 'name' (süreç adı) istedik. Daha fazlası için:
#   ['name', 'pid', 'cpu_percent', 'memory_percent', 'status']
#     name            → Sürecin adı          (örn: "chrome.exe", "python3")
#     pid             → Process ID — işletim sistemindeki kimlik numarası
#     cpu_percent     → Bu sürecin CPU kullanımı (%)
#     memory_percent  → Bu sürecin RAM kullanımı (%)
#     status          → Sürecin durumu: running, sleeping, zombie vb.
#
# process.info:
#   process_iter'e hangi alanları istedikse, o alanları sözlük (dict)
#   olarak döndürür. Örnek çıktı: {'name': 'chrome.exe'}
#
# ⚠️ Dikkat: Sistemde yüzlerce süreç olabilir; bu döngü hepsini listeler.
#    Gerçek bir uygulamada çıktıyı filtrelemek ya da bir dosyaya yazmak
#    daha pratik ve kullanışlı olacaktır.


# =============================================================================
# 🌐 BÖLÜM 6 — AĞ (NETWORK) BİLGİLERİ
# =============================================================================

net = psutil.net_io_counters()
# psutil.net_io_counters() → Sistem açıldığından bu yana (kümülatif olarak)
# tüm ağ arayüzlerinden gönderilen ve alınan toplam veri miktarını döndürür.
#
# Kümülatif nedir?
#   Bilgisayar açıldığından bugüne kadar akan toplam veridir.
#   Yalnızca son X saniyenin verisini görmek istersen, iki ölçüm arasındaki
#   farkı hesaplamak gerekir (bitiş_değeri - başlangıç_değeri).
#
# Döndürdüğü nesnenin başlıca alanları:
#   net.bytes_sent    → Gönderilen toplam veri (bayt cinsinden)
#   net.bytes_recv    → Alınan toplam veri (bayt cinsinden)
#   net.packets_sent  → Gönderilen paket sayısı
#   net.packets_recv  → Alınan paket sayısı
#   net.errin         → Alımda oluşan hata sayısı
#   net.errout        → Gönderimde oluşan hata sayısı

print(f'Gönderilen veri: {net.bytes_sent // (1024 ** 2)} MB')
# net.bytes_sent → Gönderilen veri miktarı, bayt cinsindendir.
# MB'a çevirmek için 1024² = 1.048.576'ya bölüyoruz.
# // ile tam sayıya yuvarlıyoruz (ondalık kısmı atıyoruz).
# Örnek çıktı: "Gönderilen veri: 342 MB"

print(f'Alınan veri: {net.bytes_recv // (1024 ** 2)} MB')
# net.bytes_recv → Ağdan alınan (indirilen) toplam veri miktarı.
# Aynı MB dönüşümü burada da uygulanıyor.
#
# Genellikle bytes_recv, bytes_sent'ten çok daha yüksektir.
# Neden? Web sayfaları, videolar, güncellemeler vb. indirme işlemleri
# gönderme işlemlerine kıyasla çok daha büyük veri trafiği oluşturur.


# =============================================================================
# 🔁 BÖLÜM 7 — RAM YÜKÜNÜ DÖNGÜYLE İZLEME
# =============================================================================

for i in range(3):
    # range(3) → 0, 1, 2 olmak üzere 3 adımdan oluşan bir sayı dizisi üretir.
    # Döngü her çalıştığında i sırayla 0, 1 ve 2 değerini alır.
    # Bu sayede toplam 3 kez RAM kontrolü yapılır.
    #
    # Neden 3 kez?
    #   Tek bir ölçüm yanıltıcı olabilir. Birden fazla ölçümle
    #   RAM kullanımının gerçekten sürekli yüksek mi, yoksa sadece
    #   anlık bir yükseliş mi olduğunu anlayabiliriz.
    #   Daha uzun süreli izleme için range(3) yerine
    #   range(10) veya sonsuz döngü (while True) tercih edilebilir.

    print(f'\n🔍 Kontrol {i + 1}...')
    # \n → Satır başı (newline) karakteridir.
    #       Bir önceki çıktıyla arasına görsel boşluk ekleyerek
    #       her kontrol bloğunu birbirinden ayırır.
    #
    # i + 1 → i değeri 0'dan başladığı için +1 ekleyerek
    #          kullanıcıya "Kontrol 1", "Kontrol 2", "Kontrol 3" gösteriyoruz.
    #          +1 eklemesek "Kontrol 0" çıkardı, bu daha az doğal görünür.

    ram = psutil.virtual_memory()
    # psutil.virtual_memory() her çağrıldığında anlık RAM durumunu okur.
    # Döngünün her turunda yeniden çağrılması güncel veriyi almamızı sağlar.
    # Eğer döngü dışında bir kez tanımlasaydık, hep aynı (eski) değeri görürdük.

    print(f'RAM kullanımı: {ram.percent}%')
    # ram.percent → Anlık RAM kullanım yüzdesi (float, örn: 67.3)
    # Her döngü turunda bu değer farklı olabilir; değişimi izleyebiliriz.

    if ram.percent > 60:
        # Eşik değeri (threshold) kontrolü:
        #   RAM kullanımı %60'ı geçtiyse uyarı mesajı yazdırılır.
        #   %60 eşiği burada elle (hardcoded) belirlenmiştir.
        #   İhtiyaca göre bu değeri değiştirebilirsin:
        #     > 50  → Erken uyarı (hassas sistemler için)
        #     > 75  → Orta seviye uyarı
        #     > 90  → Kritik uyarı (sistem çökmesi riski yüksek)
        print('⚠️ Uyarı! RAM kullanımı yüksek!')
        # Bu satır yalnızca if koşulu doğru (True) olduğunda çalışır.
        #
        # Gerçek bir uygulamada buraya şunlar eklenebilir:
        #   → E-posta veya anlık bildirim (notification) gönderme
        #   → Log dosyasına zaman damgasıyla kayıt etme
        #   → En çok RAM tüketen süreci otomatik kapatma (process.kill())
        #   → Sistem yöneticisine SMS gönderme

    time.sleep(5)
    # time.sleep(5) → Programı tam olarak 5 saniye boyunca duraklatır.
    #
    # Neden bekliyoruz?
    #   Her ölçüm arasında bekleme yapılmazsa döngü göz açıp kapayıncaya
    #   kadar biter ve 3 ölçüm neredeyse aynı anda alınmış olur.
    #   5 saniyelik aralıklar sayesinde RAM'deki değişimleri
    #   zaman içinde anlamlı biçimde takip edebiliriz.
    #
    # Neden 5 saniye?
    #   Çok kısa aralık (örn. 0.5 sn) → Gereksiz sık ölçüm, CPU israfı.
    #   Çok uzun aralık (örn. 60 sn)  → Hızlı yükselen bir RAM sorunu
    #                                    fark edilemeyebilir.
    #   5 saniye → İzleme için makul ve dengeli bir değerdir.
    #
    # ⚠️ Not: Son turda da (i=2) sleep çalışır, yani program bittikten
    #    sonra 5 saniye daha bekler. Son turda bekleme istemiyorsan:
    #
    #      if i < 2: 
    #          time.sleep(5)
    #
    #    şeklinde koşullu yapabilirsin.