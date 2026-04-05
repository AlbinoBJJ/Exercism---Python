class Lasagna
{

    public int ExpectedMinutesInOven()
    {    
        return 40;
    }

    public int RemainingMinutesInOven(int actualMinutes)
    {    
        return ExpectedMinutesInOven() - actualMinutes;
    }

    public int PreparationTimeInMinutes(int totalLayers)
    {
        return totalLayers * 2;
    }
    
    public int ElapsedTimeInMinutes(int totalLayers, int bakeMinutes)
    {    
        return PreparationTimeInMinutes(totalLayers) + bakeMinutes;
    }
    
}
