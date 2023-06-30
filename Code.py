import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Journals.csv')

# Prompt for a journal name
journal_name_1 = input('Enter the first journal name (CAPITAL): ')

# Filter the data for the first journal
journal_1_data = data[data['Journal name'] == journal_name_1]

# Check if the journal exists in the data
if journal_1_data.empty:
    print('Journal not found.')
else:
    # Display information of the first journal
    print('\nInformation for', journal_name_1)
    print(journal_1_data.to_string(index=False))

    # Prompt for the second journal name
    journal_name_2 = input('\nEnter the second journal name (CAPITAL) to compare: ')

    # Filter the data for the second journal
    journal_2_data = data[data['Journal name'] == journal_name_2]

    # Check if the second journal exists in the data
    if journal_2_data.empty:
        print('Second journal not found.')
    else:
        # Display information of the second journal
        print('\nInformation for', journal_name_2)
        print(journal_2_data.to_string(index=False))

        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create the bar chart for total citations comparison
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['Total Citations'].values[0], journal_2_data['Total Citations'].values[0]],
                color=['blue', 'green'])

        # Set axis labels and title
        plt.xlabel('Journal')
        plt.ylabel('Total Citations')
        plt.title('Comparison of Total Citations between Journals')

        # Display the plot
        plt.show()


        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create the bar chart for total citations comparison
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['2022 JIF'].values[0], journal_2_data['2022 JIF'].values[0]],
                color=['blue', 'green'])

        # Set axis labels and title
        plt.xlabel('Journal')
        plt.ylabel('2022 JIF')
        plt.title('Comparison of 2022 JIF between Journals')

        # Display the plot
        plt.show()

        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create the bar chart for total citations comparison
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['JIF Quartile'].values[0], journal_2_data['JIF Quartile'].values[0]],
                color=['blue', 'green'])

        # Set axis labels and title
        plt.xlabel('Journal')
        plt.ylabel('JIF Quartile')
        plt.title('Comparison of JIF Quartile between Journals')

        # Display the plot
        plt.show()

        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create the bar chart for total citations comparison
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['2022 JCI'].values[0], journal_2_data['2022 JCI'].values[0]],
                color=['blue', 'green'])

        # Set axis labels and title
        plt.xlabel('Journal')
        plt.ylabel('2022 JCI')
        plt.title('Comparison of 2022 JCI between Journals')

        # Display the plot
        plt.show()


        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create the bar chart for total citations comparison
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['% of OA Gold'].values[0], journal_2_data['% of OA Gold'].values[0]],
                color=['blue', 'green'])

        # Set axis labels and title
        plt.xlabel('Journal')
        plt.ylabel('% of OA Gold')
        plt.title('Comparison of % of OA Gold between Journals')

        # Display the plot
        plt.show()
