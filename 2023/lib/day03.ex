defmodule Aoc2023.Day03 do
  alias Aoc2023

  def part1(input) do
    %{numbers: numbers, symbols: symbols} = parse_input(input)
    symbol_positions = Map.keys(symbols)

    numbers
    |> Enum.filter(&next_to_symbol?(&1, symbol_positions))
    |> Enum.map(fn {_pos, %{length: _, number: num}} -> num end)
    |> Enum.sum()
  end

  def part2(input) do
    %{numbers: numbers, symbols: symbols} = parse_input(input)
    number_positions = numbers_covered_positions(numbers)

    symbols
    |> Map.filter(fn {_p, %{symbol: s}} -> s === "*" end)
    |> Enum.map(&elem(&1, 0))
    |> Enum.map(&adjacent_numbers(&1, number_positions))
    |> Enum.filter(fn nums -> length(nums) == 2 end)
    |> Enum.reduce(0, fn [a, b], acc -> acc + a * b end)
  end

  def example1 do
    "467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.."
    |> String.replace(" ", "")
  end

  def parse_input(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.with_index()
    |> Enum.reduce(%{numbers: %{}, symbols: %{}}, fn {row, row_no}, acc ->
      %{
        numbers: read_numbers(row, row_no, acc.numbers),
        symbols: read_symbols(row, row_no, acc.symbols)
      }
    end)
  end

  def read_numbers(row, row_no, acc) do
    numbers = Regex.scan(~r/[0-9]+/, row, return: :binary)
    indices = Regex.scan(~r/[0-9]+/, row, return: :index)

    numbers
    |> Enum.zip(indices)
    |> Enum.reduce(acc, fn {[number], [{col, length}]}, acc_enum ->
      Map.put(acc_enum, {row_no, col}, %{number: String.to_integer(number), length: length})
    end)
  end

  def read_symbols(row, row_no, acc) do
    symbols = Regex.scan(~r/[^[.0-9]+/, row, return: :binary)
    indices = Regex.scan(~r/[^[.0-9]+/, row, return: :index)

    symbols
    |> Enum.zip(indices)
    |> Enum.reduce(acc, fn {[symbol], [{col, length}]}, acc_enum ->
      Map.put(acc_enum, {row_no, col}, %{symbol: symbol, length: length})
    end)
  end

  def next_to_symbol?({position, %{length: length}}, symbol_positions) do
    position
    |> calculate_surrounding_positions(length)
    |> Enum.any?(&Enum.member?(symbol_positions, &1))
  end

  def calculate_surrounding_positions({row, col}, length \\ 1) do
    [{row, col - 1}, {row, col + length}] ++
      row_positions(row - 1, col, length) ++ row_positions(row + 1, col, length)
  end

  def row_positions(row, col, length) do
    Enum.map((col - 1)..(col + length), &{row, &1})
  end

  def numbers_covered_positions(numbers) do
    numbers
    |> Enum.reduce([], fn {{row, col}, %{number: number, length: length}}, acc ->
      positions = Enum.map(col..(col + length - 1), fn col -> {row, col} end) |> MapSet.new()
      [{number, positions} | acc]
    end)
  end

  def adjacent_numbers(position, numbers) do
    surrounding_positions =
      calculate_surrounding_positions(position)
      |> MapSet.new()

    numbers
    |> Enum.reject(fn {_number, positions} ->
      MapSet.disjoint?(positions, surrounding_positions)
    end)
    |> Enum.map(&elem(&1, 0))
  end

  def part1_ex_verify, do: example1() |> part1()
  def part2_ex_verify, do: example1() |> part2()

  def part1_verify, do: Aoc2023.input("03") |> part1()
  def part2_verify, do: Aoc2023.input("03") |> part2()
end
