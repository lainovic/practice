"""
The Abstract Factory Pattern lets you produce families of related objects without specifying their concrete classes.

:
```mermaid
classDiagram
    class AbstractFactory {
        +createStuffA() StuffA
        +createStuffB() StuffB
    }
    AbstractFactory <|-- ConcreteFactory1
    AbstractFactory <|-- ConcreteFactory2

    Client ..> AbstractFactory
```
"""

from abc import ABC, abstractmethod


class Plan:
    pass


class WorkoutPlan(Plan):
    pass


class MealPlan(Plan):
    pass


class Goal(ABC):
    @abstractmethod
    def create_workout_plan(self) -> WorkoutPlan:
        pass

    @abstractmethod
    def create_meal_plan(self) -> MealPlan:
        pass


class BuildMuscleGoal(Goal):
    def create_workout_plan(self):
        print("Workout plan for building the muscle created.")
        return WorkoutPlan()

    def create_meal_plan(self):
        print("Meal plan for building the muscle created.")
        return MealPlan()


class WeightLossGoal(Goal):
    def create_workout_plan(self):
        print("Workout plan for losing the weight created.")
        return WorkoutPlan()

    def create_meal_plan(self):
        print("Meal plan for losing the weight created.")
        return MealPlan()


class Homepage:
    def set_goal(self, Goal):
        self.workout_plan = Goal.create_workout_plan()
        self.meal_plan = Goal.create_meal_plan()


if __name__ == "__main__":
    homepage = Homepage()
    homepage.set_goal(WeightLossGoal())
    homepage.set_goal(BuildMuscleGoal())
