package delete_vowels

import "testing"

func TestDVowels(t *testing.T) {
	cases := []struct{
		name string
		value string
		want string
	}{
		{
			name: "BaseTest",
			value: "Aq",
			want: "q",
		},
		{
			name: "BaseTest",
			value: "eq",
			want: "q",
		},
		{
			name: "BaseTest",
			value: "iq",
			want: "q",
		},
		{
			name: "BaseTest",
			value: "oq",
			want: "q",
		},
		{
			name: "BaseTest",
			value: "uq",
			want: "q",
		},
	}

	for _, tc := range cases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			got :=  DeleteVowels(tc.value)

			if got != tc.want {
				t.Errorf("DeleteVowels(%v) = %v; want %v", tc.value, got, tc.want)
			}
		})
	}
}