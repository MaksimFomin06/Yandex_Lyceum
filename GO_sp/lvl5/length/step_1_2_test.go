package length

import "testing"

func TestLength(t *testing.T) {
	cases := []struct {
		name string
		value int
		want string
	}{
		{
			name: "Negative",
			value: -1,
			want: "negative",
		},
		{
			name: "Zero",
			value: 0,
			want: "zero",
		},
		{
			name: "Short",
			value: 9,
			want: "short",
		},
		{
			name: "Long",
			value: 99,
			want: "long",
		},
		{
			name: "Very long",
			value: 101,
			want: "very long",
		},
	}

	for _, tc := range cases {
		tc := tc
		t.Run(tc.name, func(t *testing.T){
			got := Length(tc.value)

			if got != tc.want {
				t.Errorf("Length(%v) = %v; want %v", tc.value, got, tc.want)
			}
		})
	}
}