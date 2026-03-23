# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Hal tersebut menjadi masalah yang cukup serius bagi institusi, karena dapat mempengaruhi reputasi serta akreditasi dari institusi tersebut

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tingkat dropout mahasiswa yang cukup tinggi setiap tahunnya. Kondisi ini menjadi perhatian serius karena dapat berdampak langsung terhadap reputasi institusi, efektivitas proses belajar-mengajar, serta efisiensi penggunaan sumber daya.

Permasalahan bisnis yang dihadapi antara lain :

* Tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikan tepat waktu atau berhenti di tengah jalan, yang berdampak pada reputasi institusi serta akreditasi kampus.

* Kurangnya pemahaman tentang faktor-faktor yang menyebabkan mahasiswa dropout, sehingga sulit untuk mengambil tindakan pencegahan yang efektif.

* Tidak adanya sistem ataupun metode yang dapat mengidentifikasi mahasiswa yang beresiko tinggi untuk dropout, yang menyebabkan keterlambatan dalam mengatasi masalah oleh kampus.

* Efek finansial dan operasional akibat dropout, seperti kehilangan pendapatan dari biaya kuliah, serta pemborosan sumber daya yang telah dikeluarkan untuk mahasiswa tersebut.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Sehingga diperlukan seorang data scientist untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Telah tersedia dataset dari pihak perusahaan untuk dianalisis. Selain itu, pihak perusahaan juga meminta untuk dibuatkan dashboard agar pihaknya mudah dalam memahami data dan memonitor performa siswa. 

Dengan memahami secara jelas permasalahan ini, Jaya Jaya Institut dapat menyusun kebijakan dan strategi berbasis data untuk menekan angka dropout dan meningkatkan kualitas pendidikan secara menyeluruh.

### Cakupan Proyek
Untuk menjawab permasalahan institut tersebut, kita akan menggunakan data yang telah dikumpulkan tersebut untuk mengembangkan sebuah sistem berbasis machine learning untuk memprediksi siswa yang mungkin bisa dropout dari institut tersebut. Pada proses pengembangannya, kita akan bereksperimen dengan berbagai pendekatan atau algoritma machine learning. 

Selain itu, kita juga akan mengembangkan sebuah prototipe sederhana dari sistem tersebut. Berikut merupakan gambaran umum dari sistem yang akan kita kembangkan.

Berdasarkan cakupan proyek tersebut, kita membutuhkan beberapa resource dan tool seperti berikut:
* Data yang disediakan oleh pihak perusahaan Jaya Jaya Institut.
* Bahasa pemrograman Python sebagai tool utama dalam proyek ini.
* Berbagai library pendukung untuk pengolahan data dan pengembangan model machine learning.
* Streamlit sebagai tool yang digunakan untuk membuat sebuah prototype sederhana.

### Persiapan

Sumber Data Sumber data yang digunakan dalam proyek ini adalah [Jaya Jaya Institut Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv).

Setup enviroment pada Shell/ Terminal dengan menggunakan perintah berikut:
```
    pip install pipenv
    pipenv install
    pipenv shell
    activate shell
```

## Business Dashboard
Dashboard pemantauan mahasiswa di **Jaya-Jaya Institut** menunjukkan gambaran umum mengenai kondisi akademik mahasiswa yang terdiri dari tiga status utama, yaitu **graduate, enrolled, dan dropout**. Berdasarkan jumlah mahasiswa, kategori **graduate merupakan yang paling banyak**, diikuti oleh **dropout**, sedangkan **enrolled** merupakan yang paling sedikit. Hal ini menunjukkan bahwa meskipun sebagian besar mahasiswa berhasil menyelesaikan studinya, jumlah mahasiswa yang mengalami **dropout masih cukup tinggi** sehingga menjadi perhatian penting bagi pihak institusi untuk melakukan pemantauan dan pencegahan.

Dilihat dari **usia saat pertama kali mendaftar (enrollment age)**, mahasiswa dengan status **dropout memiliki rata-rata usia masuk yang lebih tinggi** dibandingkan dengan mahasiswa yang masih aktif maupun yang sudah lulus. Rata-rata usia mahasiswa dropout berada di sekitar **25 tahun**, sedangkan mahasiswa enrolled dan graduate berada di kisaran **21–22 tahun**. Hal ini mengindikasikan bahwa mahasiswa yang memulai pendidikan pada usia yang lebih tua cenderung memiliki **risiko lebih besar untuk tidak menyelesaikan studi**.

Jika dilihat dari **nilai admission grade**, mahasiswa yang berstatus **graduate memiliki rata-rata nilai masuk yang sedikit lebih tinggi** dibandingkan mahasiswa enrolled dan dropout. Namun, perbedaannya tidak terlalu signifikan, sehingga dapat disimpulkan bahwa **nilai admission bukan faktor utama yang menentukan apakah seorang mahasiswa akan dropout atau tidak**. Nilai masuk hanya memberikan indikasi awal terhadap kesiapan akademik mahasiswa.

Selain faktor akademik, **faktor finansial juga terlihat memiliki pengaruh yang cukup besar terhadap dropout mahasiswa**. Mahasiswa yang berstatus dropout memiliki **tingkat pembayaran biaya kuliah yang lebih rendah** serta jumlah **tunggakan biaya kuliah yang paling tinggi** dibandingkan dengan mahasiswa yang masih aktif atau yang telah lulus. Hal ini menunjukkan bahwa **kendala finansial menjadi salah satu faktor utama yang berkaitan dengan keputusan atau kondisi mahasiswa untuk berhenti kuliah**.

Faktor lain yang terlihat dalam dashboard adalah **penerimaan beasiswa**. Mahasiswa yang berhasil lulus memiliki **proporsi penerima beasiswa yang lebih tinggi**, sedangkan mahasiswa dropout memiliki proporsi penerima beasiswa yang lebih rendah. Hal ini menunjukkan bahwa **dukungan finansial melalui beasiswa dapat membantu mahasiswa untuk bertahan hingga menyelesaikan studinya**. Sementara itu, jika dilihat dari **gender**, jumlah mahasiswa dropout antara laki-laki dan perempuan relatif **seimbang**, sehingga gender tidak terlihat sebagai faktor dominan dalam kasus dropout di institusi ini.

Secara keseluruhan, dashboard ini menunjukkan bahwa **risiko dropout mahasiswa di Jaya-Jaya Institut lebih banyak dipengaruhi oleh faktor usia saat masuk dan kondisi finansial**, seperti tunggakan biaya kuliah dan akses terhadap beasiswa, dibandingkan dengan faktor akademik awal seperti admission grade atau faktor demografis seperti gender. Oleh karena itu, pihak institusi dapat mempertimbangkan untuk meningkatkan **program dukungan finansial, pemantauan mahasiswa yang memiliki tunggakan biaya kuliah, serta pendampingan akademik bagi mahasiswa dengan risiko tinggi** untuk mengurangi tingkat dropout di masa mendatang.

Link dashboard : [klik di sini](https://public.tableau.com/app/profile/kenny.winata/viz/JayaJayaInstitutDashboard/Dashboard1?publish=yes)

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Berdasarkan hasil analisis data dan pemodelan machine learning terhadap dataset performa mahasiswa Jaya Jaya Institut, ditemukan bahwa beberapa faktor akademik dan finansial memiliki pengaruh signifikan terhadap kemungkinan mahasiswa mengalami dropout. Faktor-faktor seperti jumlah mata kuliah yang disetujui pada semester pertama dan kedua, nilai akademik, status pembayaran biaya kuliah, serta status penerima beasiswa menunjukkan korelasi yang kuat terhadap keberhasilan mahasiswa dalam menyelesaikan studinya.

Dari beberapa model machine learning yang diuji, Logistic Regression menunjukkan performa terbaik berdasarkan metrik evaluasi seperti accuracy, precision, dan recall. Selain memiliki performa yang kompetitif, Logistic Regression juga memiliki keunggulan dalam hal interpretabilitas model sehingga memudahkan institusi dalam memahami faktor risiko dropout dan mengambil keputusan berbasis data.

Dengan adanya model prediksi ini, Jaya Jaya Institut dapat melakukan deteksi dini terhadap mahasiswa yang berpotensi mengalami dropout sehingga intervensi akademik maupun non-akademik dapat dilakukan lebih cepat. Implementasi model ini diharapkan dapat membantu menurunkan angka dropout, meningkatkan tingkat kelulusan, serta meningkatkan kualitas layanan pendidikan secara keseluruhan.

### Rekomendasi Action Items
1. Implementasi sistem early warning mahasiswa berisiko dropout. Institusi disarankan untuk mengimplementasikan sistem monitoring berbasis model machine learning untuk mengidentifikasi mahasiswa yang memiliki risiko tinggi mengalami dropout sejak semester awal. Dengan adanya sistem peringatan dini ini, pihak akademik dapat melakukan intervensi lebih cepat seperti pemanggilan mahasiswa, pemberian konseling akademik, atau pendampingan belajar sehingga risiko dropout dapat diminimalkan.

2. Peningkatan program bimbingan akademik. Mahasiswa yang memiliki performa akademik rendah, khususnya pada semester pertama dan kedua, sebaiknya mendapatkan perhatian khusus melalui program mentoring atau tutoring. Institusi dapat menyediakan program bimbingan tambahan, kelas remedial, atau pendampingan oleh dosen pembimbing akademik untuk membantu meningkatkan performa belajar mahasiswa tersebut.

3. Dukungan finansial bagi mahasiswa yang mengalami kesulitan ekonomi. Hasil analisis menunjukkan bahwa faktor finansial seperti keterlambatan pembayaran biaya kuliah dapat menjadi indikator risiko dropout. Oleh karena itu, institusi dapat mempertimbangkan pemberian skema pembayaran fleksibel, bantuan finansial, atau perluasan program beasiswa bagi mahasiswa yang mengalami kendala ekonomi agar mereka tetap dapat melanjutkan pendidikan.

4. Monitoring performa akademik secara berkala melalui dashboard. Institusi disarankan untuk memanfaatkan dashboard monitoring yang telah dibuat untuk memantau performa mahasiswa secara berkala. Dashboard ini dapat digunakan oleh pihak manajemen maupun dosen untuk melihat tren performa akademik, distribusi risiko dropout, serta faktor-faktor yang mempengaruhi keberhasilan studi mahasiswa sehingga keputusan akademik dapat lebih berbasis data.

5. Pengembangan program student engagement dan well-being. Selain faktor akademik dan finansial, keterlibatan mahasiswa dalam lingkungan kampus juga dapat mempengaruhi keberhasilan studi. Oleh karena itu, institusi dapat meningkatkan program engagement seperti kegiatan organisasi mahasiswa, seminar pengembangan diri, layanan konseling psikologis, serta program kesejahteraan mahasiswa untuk meningkatkan motivasi belajar dan rasa keterikatan mahasiswa terhadap institusi.
