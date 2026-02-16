package main

import "testing"

func TestGetUTFLength(t *testing.T) {
	cases := []struct{
		name string
		value []byte
		want int
	}{
		{
			name:    "Base ASCII",
			value:   []byte("hello"),
			want:    5,
		},
		{
			name:    "Cyrillic chars",
			value:   []byte("привет"),
			want:    6,
		},
		{
			name:    "Emoji",
			value:   []byte("👋🌍"),
			want:    2,
		},
		{
			name:    "Empty string",
			value:   []byte(""),
			want:    0,
		},
		{
			name:    "Invalid UTF8",
			value:   []byte{0xff, 0xfe},
			want:    0,
		},
	}

	for _, tc := range cases {
		tc := tc
		t.Run(tc.name, func(t *testing.T){
			got, _ := GetUTFLength(tc.value)

			if got != tc.want {
				t.Errorf("GetUTFLength(%v) = %v; want %v", tc.value, got, tc.want)
			}
		})
	}
}