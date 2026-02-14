package multiply

import "testing"

func TestMultiply(t *testing.T) {
	cases := []struct {
		name string
		values []int
		want int
	}{
		{
			name: "Positive numbers",
			values: []int{10, 2},
			want: 5,
		},
		{
			name: "Negative numbers",
			values: []int{-10, -2},
			want: 5,
		},
	}

	for _, tc := range cases {
		tc := tc
		t.Run(tc.name, func(t *testing.T){
			got := Multiply(tc.values[0], tc.values[1])

			if got != tc.want {
				t.Errorf("Multiply(%v) = %v; want %v", tc.values, got, tc.want)
			}
		})
	}
}