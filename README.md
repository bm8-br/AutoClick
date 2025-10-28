# Auto Click Sequence Hotkey

## Features

- Record multiple mouse positions  
- Auto-click them in sequence  
- Stop safely with **F8** or moving to `(0,0)`  
- Delay between clicks for smooth automation  
- Clear terminal messages showing progress  

---

## Requirements

Install dependencies first:

```bash
pip install pyautogui pynput
```

---

## How to Use

1. **Run the script:**
   ```bash
   python auto_click_sequence_hotkey.py
   ```

2. **Record points:**
   - Move your mouse to a point and press **Enter** to save it.  
   - Type **“fim”** (or `end`) and press **Enter** when done.

3. **Start clicking:**
   - The script waits **3 seconds**, then begins clicking the saved points repeatedly.  
   - You can stop anytime.

4. **Stop automation:**
   - Press **F8**, or  
   - Move your mouse to the top-left corner `(0,0)`.

---

## Code Overview

- **`capturar_pontos()`** – records mouse positions.  
- **`on_press()`** – listens for **F8** to stop safely.  
- **`loop_cliques()`** – performs the automatic clicking loop.  
- **Main block** – runs everything in order.

---

## Notes

- The script clicks wherever your mouse is focused — use it carefully.  
- Test it in a safe environment first.  
- Moving to `(0,0)` always stops it immediately.
