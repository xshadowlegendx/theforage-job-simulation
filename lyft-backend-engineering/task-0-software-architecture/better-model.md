---
title: lyft-rental
---
classDiagram
    class CarEngine {
        +Int id
        +String name
        +Int maxMileage
        +Int lastMileage
        +Boolean isWarningLightOn
        +DateTime manufacturedAt

        +serviceDate() DateTime
    }

    class CarBattery {
        +Int id
        +String name
        +Int serviceTimeAsDays
        +DateTime manufacturedAt

        +serviceDate() DateTime
    }

    class Car {
        +Int id
        +String name
        +CarEngine engine
        +CarBattery battery

        +isNeedService() bool
    }

    Car<--CarEngine
    Car<--CarBattery

