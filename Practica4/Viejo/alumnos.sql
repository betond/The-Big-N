-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2021 at 06:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumnos`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumnodatos`
--

CREATE TABLE `alumnodatos` (
  `Id` varchar(15) NOT NULL,
  `Nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `ApellidoP` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `ApellidoM` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `FechaN` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Genero` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `CURP` varchar(25) COLLATE utf8_spanish_ci NOT NULL,
  `Calle` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Colonia` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Alcaldia` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `CodigoPostal` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `Telefono` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `Correo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `EscuelaProcedencia` varchar(25) COLLATE utf8_spanish_ci NOT NULL,
  `EntidadProcedencia` varchar(20) COLLATE utf8_spanish_ci NULL,
  `NombreEscuela` varchar(50) COLLATE utf8_spanish_ci NULL,
  `Promedio` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `EscomOpcion` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `Grupo` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `Hora` varchar(10) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumnodatos`
--
ALTER TABLE `alumnodatos`
  ADD PRIMARY KEY (`Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
