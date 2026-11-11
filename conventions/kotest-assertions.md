# Kotest Assertions

## Цепочки проверок

В цепочке проверок объединяй только вызовы `should*`:

```kotlin
name.shouldStartWith("М")
    .shouldHaveLength(5)
```

Не продолжай такую цепочку обычными методами.
Плохо:

```kotlin
val attempt = attempts.shouldHaveSize(1).single()
```

Если извлечение данных зависит от успешной проверки, выполни проверку и извлечение отдельными выражениями:

```kotlin
attempts shouldHaveSize 1
val attempt = attempts.single()
```

Если данные нужны только для дальнейших проверок, используй блок соответствующего матчера:

```kotlin
attempts.shouldBeSingleton { attempt ->
    attempt.responseStatus shouldBe 201
}
```
