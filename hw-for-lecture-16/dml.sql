INSERT INTO guests (guest_id, name, email, phone_number, language)
VALUES
    (1, 'John Doe', 'john.doe@example.com', '123-456-7890', 'English'),
    (2, 'Jane Smith', 'jane.smith@example.com', '987-654-3210', 'Spanish'),
    (3, 'Bob Johnson', 'bob.johnson@example.com', '555-123-4567', 'French');
INSERT INTO hosts (host_id, name, email, phone_number)
VALUES
    (1, 'Host1', 'host1@example.com', '111-222-3333'),
    (2, 'Host2', 'host2@example.com', '444-555-6666');
INSERT INTO rooms (room_id, host_id, location, air_conditioning, refrigerator, pet_friendly, breakfast, transfer, price)
VALUES
    (1, 1, 'City Center', true, true, false, true, false, 100),
    (2, 1, 'Suburb Retreat', false, true, true, false, true, 80),
    (3, 2, 'Cozy Cottage', true, false, true, true, true, 120);
INSERT INTO reservations (reservation_id, guest_id, host_id, room_id, checkin_date, checkout_date, payment_status)
VALUES
    (1, 1, 1, 1, '2023-01-01', '2023-01-05', 'Paid'),
    (2, 2, 1, 2, '2023-02-01', '2023-02-07', 'Pending'),
    (3, 3, 2, 3, '2023-03-15', '2023-03-20', 'Paid'),
    (4, 3, 1, 1, '2023-03-18', '2023-03-20', 'Paid');
INSERT INTO payments (payments_id, reservation_id, payment_date, amount)
VALUES
    (1, 1, '2023-03-02', 100.00),
    (2, 3, '2023-03-16', 120.00),
    (3, 2, '2023-02-05', 80.00),
    (4, 4, '2023-03-18', 25.00);