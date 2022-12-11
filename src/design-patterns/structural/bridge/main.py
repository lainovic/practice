"""
Bridge lets you split a set of closely related classes into separate hierarchies that are coupled,
but can also be developed independently of each other.
In a way, the "bridge" is placed between the two base abstractions.

By doing this, we avoid creating a bunch of classes by combining all the options and asigning a class to each combination,
which would result in having as many classes as combinations, i.e. a product of all varying factors.
With bridge pattern, we replace multiplication with addition as we will have as many classes as there are varying factors,
and then we can couple them at runtime to produce all the combinations.


```mermaid
classDiagram
class Service {
    <<abstract>>
    +start()
    +stop()
}
ServiceA --|> Service
ServiceB --|> Service
class Device {
    <<abstract>>
    +data()
}
Service o-- Device : uses
DeviceX --|> Device
DeviceY --|> Device
```
"""

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_channel(self, num):
        pass


class RemoteControl:
    def __init__(self, device) -> None:
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


class AdvancedRemoteControl(RemoteControl):
    def __init__(self, device) -> None:
        super().__init__(device)

    def set_channel(self, num):
        self.device.set_channel(num)


class SonyTV(Device):
    def turn_on(self):
        print("Sony: turn on.")

    def turn_off(self):
        print("Sony: turn off.")

    def set_channel(self, num):
        print(f"Sony: set channel {num}.")


class SamsungTV(Device):
    def turn_on(self):
        print("Samsung: turn on.")

    def turn_off(self):
        print("Samsung: turn off.")

    def set_channel(self, num):
        print(f"Samsung: set channel {num}.")


if __name__ == "__main__":
    remote_ctrl = RemoteControl(SonyTV())
    remote_ctrl.turn_on()
    remote_ctrl.turn_off()
    adv_remote_ctrl = AdvancedRemoteControl(remote_ctrl.device)
    adv_remote_ctrl.turn_on()
    adv_remote_ctrl.turn_off()
    adv_remote_ctrl.set_channel(5)
    adv_remote_ctrl.device = SamsungTV()
    adv_remote_ctrl.turn_on()
    adv_remote_ctrl.turn_off()
    adv_remote_ctrl.set_channel(12)
