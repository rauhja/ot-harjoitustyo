sequenceDiagram
    Main->>Machine: Machine()
    Machine ->> Fueltank: Fueltank()
    Machine ->> Fueltank: tank.fill(40)
    Fueltank ->> Engine: Engine()
    Main ->> Machine: drive()
    Machine ->> Engine: engine.start()
    Engine ->> Fueltank: tank.consume(5)
    Machine ->> Engine: engine.is_running()
    Engine ->> Fueltank: tank.fuel_contents > 0
    Fueltank ->> Engine: true
    Engine ->> Fueltank: tank.consume(10)