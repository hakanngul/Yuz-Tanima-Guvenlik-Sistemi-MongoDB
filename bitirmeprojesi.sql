-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 20 Ara 2020, 18:35:52
-- Sunucu sürümü: 10.4.16-MariaDB
-- PHP Sürümü: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `bitirmeprojesi`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kisi`
--

CREATE TABLE `kisi` (
  `id` varchar(200) NOT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email_adres` varchar(50) DEFAULT NULL,
  `telefon` varchar(11) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `kisi`
--

INSERT INTO `kisi` (`id`, `full_name`, `username`, `password`, `email_adres`, `telefon`, `role`) VALUES
('1', 'testname lastname', 'test', '123456', 'test@gmail.com', '5317328099', 'admin'),
('uuid.uuid4()', '1 2', '3', '4', '5', '5317328099', 'admin'),
('d2f619dcfd7a4276a06c34243013ad57', 'yusuf bolum', 'ybolum', '123123', 'yusuf@gmail.com', '5317328099', 'admin'),
('65eebf85ee8f48b49a6835027570a94a', 'hakan gul', 'hakn', '123123', 'asda@gmail.com', '5317328099', 'vardiyasorumlusu'),
('633b426d5fdc4da291b0e53b8d6772d3', 'asdas asdas', 'test1', '123123', 'sdafsdf', '5317328099', 'admin'),
('65ee6d1d21ca4182a1b449197b210e4b', 'tes asdas', 'test232', '123123', 'adkfjaksdfjsdkl', '5317328099', 'vardiyasorumlusu'),
('c2a91e350cff409aac5a1152e6706167', 'teasd asdas', 'test1', '123123', 'asdfdsfasf', '5317328099', 'vardiyasorumlusu'),
('51bdc55446a74e378b49d600beccc093', 'asdas asdas', 'test2321', '123123', 'sdfgsdfg', '5317328099', 'vardiyasorumlusu'),
('21fb55af39844562afe6cc2c1cf7f3da', 'asdas dasdasd', 'hakangul1', '123123', 'self.email_adres', '5317328099', 'admin'),
('8a2e46f59a1548ad998792ba695ca86f', 'asdasd asdas', 'hakangul23', '123123', 'dfdsfgsdfg', '5317328099', 'admin'),
('afeff997702e4c95a11d4ebced913961', 'saf asdf', 'test23231', '123123', 'gfdfgsdgdf', '5317328099', 'admin'),
('3a7650c551794ee2bfde869c11997049', 'asdasd asdasd', 'hasjkdhasjk', '123123', 'fgdgdfg', '5317328099', 'admin');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `rapor`
--

CREATE TABLE `rapor` (
  `id` int(11) NOT NULL,
  `isci_id` int(11) DEFAULT NULL,
  `vardiyaDurum` varchar(10) DEFAULT NULL,
  `toplamCalismaGun` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `admin` varchar(10) DEFAULT NULL,
  `vSorumlu` varchar(10) DEFAULT NULL,
  `isci` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `vardiya`
--

CREATE TABLE `vardiya` (
  `id` int(11) NOT NULL,
  `sabah` varchar(10) DEFAULT NULL,
  `aksam` varchar(10) DEFAULT NULL,
  `gece` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `rapor`
--
ALTER TABLE `rapor`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `vardiya`
--
ALTER TABLE `vardiya`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `rapor`
--
ALTER TABLE `rapor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `vardiya`
--
ALTER TABLE `vardiya`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
