#[macro_export]
macro_rules! decode_tests {
    ($($func_name:ident, $name:ident: $value:expr,)*) => {
        $(
            #[test]
            fn $name() {
                let (input, expected) = $value;
                assert_eq!(expected, $func_name(input));
            }
        )*
    }
}
