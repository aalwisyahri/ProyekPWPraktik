-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2025 at 09:50 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pw_praktik`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(150) NOT NULL,
  `role` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password_hash` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `role`, `email`, `password_hash`) VALUES
(1, 'admin', 'admin', 'user@admin.com', 'pbkdf2:sha256:1000000$8I3oVxHSQIelbOlv$adf70830d3499e2140420b9af466bdd488dc180fd4ecca76b86aa9b2948b3d92'),
(2, 'asep', 'user', 'asep@user.com', 'pbkdf2:sha256:1000000$r2V1mXFcD4kCG4sd$252b79e9d87f170bad2d42c5a1b3047c05680da9898bf2fc83a18efc8abab35e'),
(3, 'alex', 'user', 'alex@user.com', 'pbkdf2:sha256:1000000$UfJYRHkkVGgp06Vz$5fa4e67c1a50595148b4f059ccbe66324abcb9eacebd359b3916f5c7bcfb9041'),
(4, 'mealw', 'admin', 'mealw@admin.com', 'pbkdf2:sha256:1000000$auvmDbiJESDkq268$c050750ff4e7e5534a875fd59cec7af7183344ca8f9b45929de0585a562e69f9'),
(5, 'xm', 'admin', 'xm@admin.com', 'pbkdf2:sha256:1000000$PKh3x86OOudfT0QG$86ab52a364a107d61248e49b73a20574fb587fb96bfb04df9a246fcaca767de8'),
(6, 'josh', 'user', 'josh@user.com', 'pbkdf2:sha256:1000000$QK5vy6R1PXrobUMm$2569cbd1ec46dbd473e65abe404750a97eaeacc0b367a181c60d77320ba5c731'),
(7, 'alwi', 'admin', 'alwi@admin.com', 'pbkdf2:sha256:1000000$1Fo82elUZPfIZuYA$47ccdbae2a942471cf22a21c6b8f0ab22292e6b5724ecfdd1a423cf5df88d050');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
