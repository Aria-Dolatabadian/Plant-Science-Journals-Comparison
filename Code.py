import pandas as pd
import matplotlib.pyplot as plt


#Read the CSV file
data = pd.read_csv('Journals.csv')

#Prompt for a journal name
journal_name_1 = input('Enter the first journal name (CAPITAL): ')

#Filter the data for the first journal
journal_1_data = data[data['Journal name'] == journal_name_1]

#Check if the journal exists in the data
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
        plt.figure(figsize=(10, 12))

        # Create subplots for all comparisons
        plt.subplot(5, 2, 1)
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['Total Citations'].values[0], journal_2_data['Total Citations'].values[0]],
                color=['blue', 'green'])
        # plt.xlabel('Journal')
        plt.ylabel('Total Citations')
        plt.title('Comparison of Total Citations between Journals')

        plt.subplot(5, 2, 2)
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['2022 JIF'].values[0], journal_2_data['2022 JIF'].values[0]],
                color=['blue', 'green'])
        # plt.xlabel('Journal')
        plt.ylabel('2022 JIF')
        plt.title('Comparison of 2022 JIF between Journals')

        plt.subplot(5, 2, 3)
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['JIF Quartile'].values[0], journal_2_data['JIF Quartile'].values[0]],
                color=['blue', 'green'])
        # plt.xlabel('Journal')
        plt.ylabel('JIF Quartile')
        plt.title('Comparison of JIF Quartile between Journals')

        plt.subplot(5, 2, 4)
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['2022 JCI'].values[0], journal_2_data['2022 JCI'].values[0]],
                color=['blue', 'green'])
        plt.xlabel('Journal')
        plt.ylabel('2022 JCI')
        plt.title('Comparison of 2022 JCI between Journals')

        plt.subplot(5, 2, 5)
        plt.bar([journal_name_1, journal_name_2],
                [journal_1_data['% of OA Gold'].values[0], journal_2_data['% of OA Gold'].values[0]],
                color=['blue', 'green'])
        plt.xlabel('Journal')
        plt.ylabel('% of OA Gold')
        plt.title('Comparison of % of OA Gold between Journals')

        # Adjust spacing between subplots
        plt.tight_layout()

        # Display the plot
        plt.show()

