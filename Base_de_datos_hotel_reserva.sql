-- Tabla para almacenar la información del hotel
CREATE TABLE Hotel (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    categoria VARCHAR(50)
);

-- Tabla para almacenar la información de las habitaciones
CREATE TABLE Habitacion (
    habitacion_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_id INT,
    tipo VARCHAR(50),
    capacidad INT,
    precio DECIMAL(10, 2),
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

-- Tabla para almacenar la información de los clientes
CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    correo_electronico VARCHAR(255),
    telefono VARCHAR(20)
);

-- Tabla para almacenar la información de las reservas
CREATE TABLE Reserva (
    reserva_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    habitacion_id INT,
    fecha_entrada DATE,
    fecha_salida DATE,
    cantidad_personas INT,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (habitacion_id) REFERENCES Habitacion(habitacion_id)
);

-- Tabla para registrar los métodos de pago
CREATE TABLE MetodoPago (
    metodo_pago_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100)
);

-- Tabla para registrar las transacciones de pago de las reservas
CREATE TABLE PagoReserva (
    pago_id INT PRIMARY KEY AUTO_INCREMENT,
    reserva_id INT,
    metodo_pago_id INT,
    monto_pagado DECIMAL(10, 2),
    fecha_pago DATE,
    FOREIGN KEY (reserva_id) REFERENCES Reserva(reserva_id),
    FOREIGN KEY (metodo_pago_id) REFERENCES MetodoPago(metodo_pago_id)
);

-- Tabla para almacenar las categorías de habitaciones
CREATE TABLE CategoriaHabitacion (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT
);

-- Tabla para almacenar el historial de precios de las habitaciones
CREATE TABLE HistorialPrecio (
    historial_id INT PRIMARY KEY AUTO_INCREMENT,
    habitacion_id INT,
    precio_anterior DECIMAL(10, 2),
    fecha_actualizacion DATE,
    FOREIGN KEY (habitacion_id) REFERENCES Habitacion(habitacion_id)
);
