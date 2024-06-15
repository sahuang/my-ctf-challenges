package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

const (
	accuracyPortion = 0.3
	comboPortion    = 0.7
	thresholdScore  = 1099727 // Threshold score required to unlock the flag
)

func calculateScore(accuracy, combo, maxAchievableCombo, modeBonus float64, currentTime int64) float64 {
	// Introduce a time-dependent modifier based on time % 727
	timeModifier := float64(currentTime%727) / 727

	// Modify accuracy and combo based on the time modifier
	adjustedAccuracy := accuracy + (1-accuracy)*timeModifier
	adjustedCombo := combo + (maxAchievableCombo-combo)*timeModifier

	// Calculate v3 score
	totalScore := 1000000 * ((adjustedAccuracy * accuracyPortion) + (adjustedCombo / maxAchievableCombo * comboPortion))
	totalScore *= modeBonus

	return totalScore
}

func parseInput(input string) (modeBonus, accuracy, combo, maxAchievableCombo float64, err error) {
	parts := strings.Fields(input)

	// Parse mode, can be HD, HR or DT
	switch parts[0] {
	case "HD":
		modeBonus = 1.06
	case "HR":
		modeBonus = 1.08
	case "DT":
		modeBonus = 1.1
	default:
		err = fmt.Errorf("bad input")
		return
	}

	// Parse accuracy
	accuracyStr := strings.TrimSuffix(parts[1], "%")
	accuracy, err = strconv.ParseFloat(accuracyStr, 64)
	if err != nil || accuracy < 0 || accuracy > 95 {
		err = fmt.Errorf("bad input")
		return
	}
	accuracy /= 100

	// Parse combo
	comboParts := strings.Split(strings.TrimSuffix(parts[2], "x"), "/")
	combo, err = strconv.ParseFloat(comboParts[0], 64)
	if err != nil {
		err = fmt.Errorf("bad input")
		return
	}
	maxAchievableCombo, err = strconv.ParseFloat(comboParts[1], 64)
	if err != nil || maxAchievableCombo != 1200 || combo > 1000 {
		err = fmt.Errorf("bad input")
		return
	}

	return
}

func main() {
	// input := "DT 95% 1000/1200x"
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	modeBonus, accuracy, combo, maxAchievableCombo, err := parseInput(input)
	if err != nil {
		return
	}

	currentTime := time.Now().Unix()

	// Check if the player's score meets the threshold for the flag
	if int(calculateScore(accuracy, combo, maxAchievableCombo, modeBonus, currentTime)) >= thresholdScore {
		flag, err := os.ReadFile("flag.txt")
		if err != nil {
			fmt.Println("Error reading flag file:", err)
			return
		}
		fmt.Println("Congratulations! Here is your flag:", string(flag))
	} else {
		fmt.Println("Keep trying!")
	}
}
