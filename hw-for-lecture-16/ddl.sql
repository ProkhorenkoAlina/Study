CREATE TABLE "guests" (
	"guest_id" serial NOT NULL,
	"name" varchar(50) NOT NULL,
	"email" varchar(50) NOT NULL,
	"phone_number" varchar(15) NOT NULL,
	"language" varchar(20) NOT NULL DEFAULT 'English',
	CONSTRAINT "guests_pk" PRIMARY KEY ("guest_id")
);
CREATE TABLE "hosts" (
	"host_id" serial NOT NULL,
	"name" varchar(50) NOT NULL,
	"email" varchar(50) NOT NULL,
	"phone_number" varchar(15) NOT NULL,
	CONSTRAINT "hosts_pk" PRIMARY KEY ("host_id")
);
CREATE TABLE "rooms" (
	"room_id" serial NOT NULL,
	"host_id" integer NOT NULL,
	"location" varchar(100) NOT NULL,
	"air_conditioning" BOOLEAN NOT NULL,
	"refrigerator" BOOLEAN NOT NULL,
	"pet_friendly" BOOLEAN NOT NULL,
	"breakfast" BOOLEAN NOT NULL,
	"transfer" BOOLEAN NOT NULL,
	"price" integer NOT NULL,
	CONSTRAINT "rooms_pk" PRIMARY KEY ("room_id")
);
CREATE TABLE "reservations" (
	"reservation_id" serial UNIQUE NOT NULL,
	"guest_id" integer NOT NULL,
	"host_id" integer NOT NULL,
	"room_id" integer NOT NULL,
	"checkin_date" DATE NOT NULL,
	"checkout_date" DATE NOT NULL,
	"payment_status" varchar NOT NULL,
	CONSTRAINT "reservations_pk" PRIMARY KEY ("reservation_id", "guest_id","host_id","room_id")
);
CREATE TABLE "payments" (
	"payments_id" serial NOT NULL,
	"reservation_id" integer NOT NULL,
	"payment_date" DATE NOT NULL,
	"amount" FLOAT NOT NULL,
	CONSTRAINT "payments_pk" PRIMARY KEY ("payments_id")
);

ALTER TABLE "rooms" ADD CONSTRAINT "rooms_fk0" FOREIGN KEY ("host_id") REFERENCES "hosts"("host_id");
ALTER TABLE "reservations" ADD CONSTRAINT "reservations_fk0" FOREIGN KEY ("guest_id") REFERENCES "guests"("guest_id");
ALTER TABLE "reservations" ADD CONSTRAINT "reservations_fk1" FOREIGN KEY ("host_id") REFERENCES "hosts"("host_id");
ALTER TABLE "reservations" ADD CONSTRAINT "reservations_fk2" FOREIGN KEY ("room_id") REFERENCES "rooms"("room_id");
ALTER TABLE "payments" ADD CONSTRAINT "payments_fk0" FOREIGN KEY ("reservation_id") REFERENCES "reservations"("reservation_id");