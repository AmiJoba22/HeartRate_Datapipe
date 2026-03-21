1. Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

- The file [phase1.txt](data/phase1.txt) represented the most active period as it contained the highest average of 87.3 bpm and the highest median of 88.5 bpm.

- These rates describe the typical variability in this file but are less than the target heart rate for a 30 year old.

- This could indicate healthier heart muscles in this participant, as their rate can typically be lower than the target.

2. Which file had the **poorest** data quality? How do you know?

- The file [phase0.txt](data/phase0.txt) had the poorest data quality due to the fact that it had the most removed values. Some values were either missing or were listed as 'NO DATA'.

3. Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.

- Maximum Value: 180
- Minimum Value: 68
- Range: 112

b) Explain how the extreme value affects the range.

- The extremity of the maximum value is likely to increase the range significantly, if the minimum value isn't in close range to maximum. This causes the data to be spread out more.

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

- The median is a better representation of the dataset's typical variability. It won't be influenced by the outlier since its the center point and relies on middle positioning to be identified.
