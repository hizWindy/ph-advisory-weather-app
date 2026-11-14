Weather Alert Rules & Thresholds 

Note: Our heat levels use PAGASA's heat index table as a general guide, but because we rely on third-party forecast data (Open-Meteo), our values should be treated and labeled as an estimate.

1. Rain Rule

An hourly forecast slot is classified as Rainy when the precipitation probability meets or exceeds the threshold below:

Rainy Hour Threshold: precipitation_probability >= 60%

Not Rainy: precipitation_probability < 60%

2. Heat Check Rules (Estimated Heat Index)

The Heat Check feature evaluates the hourly feels-like temperature (apparent_temperature) and maps it to one of three user-friendly status levels, paired with actionable safety tips.

Thresholds & Safety Tips
Heat Level | Feels-Like Temperature ($^\circ\text{C}$)                    | User-Facing Tip/ Action

Ok         | < 33°C (Below $33^\circ\text{C}$)                            | Weather is comfortable. Stay hydrated as usual.
Mag-ingat  | 33°C to 41°C ($33^\circ\text{C} \le T \le 41^\circ\text{C}$) |Drink more water, wear light clothing, and take breaks in the shade.
Delikado   | >= 42°C ($42^\circ\text{C}$ and above)                       | Stay out of the noon sun (10:00 AM – 4:00 PM), limit strenuous outdoor activity, and hydrate frequently.

(Note: PAGASA classifies $27^\circ\text{C}$–$32^\circ\text{C}$ as "Caution" and $33^\circ\text{C}$–$41^\circ\text{C}$ as "Extreme Caution." For our simplified 3-tier app model, anything below $33^\circ\text{C}$ is grouped under OK, $33^\circ\text{C}$–$41^\circ\text{C}$ maps to Mag-ingat, and $42^\circ\text{C}+$ maps to Delikado).

3. Examples
    1. Feels like $30^\circ\text{C}$ $\rightarrow$ OK (Tip: Weather is comfortable. Stay hydrated as usual.)
    2. Feels like $38^\circ\text{C}$ $\rightarrow$ Mag-ingat (Tip: Drink more water and take breaks in the shade.)
    3. Feels like $44^\circ\text{C}$ $\rightarrow$ Delikado (Tip: Stay out of the noon sun and limit outdoor activity.)
    4. Rain chance is $75\%$ $\rightarrow$ Rainy (Meets the $\ge 60\%$ threshold)
    5. Rain chance is $40\%$ and feels like $41^\circ\text{C}$ $\rightarrow$ Not Rainy + Mag-ingat
    