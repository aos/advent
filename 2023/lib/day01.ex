defmodule Aoc2023.Day01 do
  alias Aoc2023

  @valid_digits %{
    "one" => "1",
    "two" => "2",
    "three" => "3",
    "four" => "4",
    "five" => "5",
    "six" => "6",
    "seven" => "7",
    "eight" => "8",
    "nine" => "9"
  }

  def part1(inp) do
    inp
    |> String.split("\n", trim: true)
    |> Enum.map(&to_integer/1)
    |> Enum.sum()
  end

  def part2(inp) do
    inp
    |> String.split("\n", trim: true)
    |> Enum.map(&part2_to_integer/1)
    |> Enum.sum()
  end

  def example_one do
    "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"
  end

  def example_two do
    "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"
  end

  defp to_integer(string) do
    numbers = Regex.replace(~r/[a-z]/, string, "")
    String.to_integer("#{String.first(numbers)}#{String.last(numbers)}")
  end

  defp part2_to_integer(string) do
    numbers =
      find_all_nums(string, Enum.map(0..9, &to_string/1) ++ Map.keys(@valid_digits))
      |> Enum.filter(& &1)

    String.to_integer("#{List.first(numbers)}#{List.last(numbers)}")
  end

  defp find_all_nums("", _matches), do: []

  defp find_all_nums(string, matches) do
    [
      as_number(Enum.find(matches, &String.starts_with?(string, &1)))
      | find_all_nums(String.slice(string, 1..-1//1), matches)
    ]
  end

  defp as_number(val), do: Map.get(@valid_digits, val, val)
end
