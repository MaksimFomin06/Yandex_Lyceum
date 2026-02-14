package sum

import "testing"

func TestSum(t *testing.T) {
		cases := []struct {
		name string
		values []int
		want int
	}{
		{
		name: "Positive values",
		values: []int{2, 2},
		want: 4,
		},
		{
			name: "Negative numbers",
			values: []int{-2, -2},
			want: -4,
		},
		{
			name: "Mixed values",
			values: []int{-2, 2},
			want: 0,
		},
	}

	for _, tc := range cases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			got := Sum(tc.values[0], tc.values[1])

			if got != tc.want {
				t.Errorf("Sum(%v) = %v; want %v", tc.values, got, tc.want)
			}
		})
	}
}