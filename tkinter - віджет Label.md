# tkinter - віджет Label

`Label` (мітка) — віджет для відображення тексту у вікні. Він використовується, коли потрібно показати підпис, заголовок чи коротке повідомлення в інтерфейсі.

## Приклад:

```python
from tkinter import *

window = Tk()
window.geometry("150x50")

label = Label(text="Привіт, світе!", bg="yellow", fg="blue")
label.pack()

window.mainloop()
```

Результат:

![Результат](tkinter%20-%20віджет%20Label/1.png)


У прикладі мітка одразу отримує основні властивості - `text` задає напис, `bg` встановлює фон мітки, а `fg` — колір тексту.

## Поширені властивості Label

| Властивість | Опис | Приклад |
| --- | --- | --- |
| `text` | Текст мітки | `Label(text="Привіт!")` |
| `bg` | Фоновий колір | `Label(text="Привіт!", bg="yellow")` |
| `fg` | Колір тексту | `Label(text="Привіт!", fg="blue")` |
| `font` | Шрифт (назва, розмір) | `Label(text="Привіт!", font=("Arial", 16))` |
| `width` | Ширина у символах | `Label(text="Привіт!", width=20)` |
| `height` | Висота у символах | `Label(text="Привіт!", height=2)` |
| `padx`, `pady` | Внутрішні відступи | `Label(text="Привіт!", padx=10, pady=5)` |
| `anchor` | Вирівнювання вмісту (`"n"`, `"s"`, `"e"`, `"w"`, `"ne"`, `"nw"`, `"se"`, `"sw"`, `"center"`) | `Label(text="Привіт!", anchor="w")` |
| `justify` | Вирівнювання рядків тексту (`"left"`, `"right"`, `"center"`) | `Label(text="Привіт!", justify="left")` |
| `wraplength` | Ширина переносу тексту | `Label(text="Привіт!", wraplength=6)` |

